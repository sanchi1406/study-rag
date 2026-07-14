import { useState } from "react";
import api from "../services/api";

function Chat() {

    const [question, setQuestion] = useState("");

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    const handleSend = async () => {

        if(question.trim()==="") return;

        const userMessage = {
            type:"user",
            text:question
        };

        setMessages(prev=>[
            ...prev,
            userMessage
        ]);

        setLoading(true);

        try{

            const response = await api.post("/chat",{
                question:question
            });

            const botMessage={
                type:"bot",
                text:response.data.answer,
                warning:response.data.warning,
                sources:response.data.sources
            };

            setMessages(prev=>[
                ...prev,
                botMessage
            ]);

            setQuestion("");

        }

        catch(error){

            setMessages(prev=>[
                ...prev,
                {
                    type:"bot",
                    text:"Something went wrong."
                }
            ]);

            console.log(error);

        }

        finally{

            setLoading(false);

        }

    };

    return(

        <div className="chat-page">
            <div className="chat-logo">

    <img
         src="/bot.png"
        alt="AI Assistant"
    />

</div>

            <h1 className="chat-heading">

                AI Study Assistant

            </h1>

            <div className="chat-box">

                {messages.map((msg,index)=>(

                    <div
                        key={index}
                        className={
                            msg.type==="user"
                            ?
                            "user-message"
                            :
                            "bot-message"
                        }
                    >

                        <p>{msg.text}</p>

                        {
                            msg.warning &&
                            <div className="warning">

                                {msg.warning}

                            </div>
                        }

                        {
                            msg.sources &&
                            msg.sources.length>0 &&

                            <div className="sources">

                                <h4>Sources</h4>

                                {
                                    msg.sources.map((source,i)=>(

                                        <p key={i}>

                                            📄 {source.source}

                                        </p>

                                    ))
                                }

                            </div>

                        }

                    </div>

                ))}

            </div>

            <div className="chat-input">

                <input

                    value={question}

                    onChange={(e)=>setQuestion(e.target.value)}

                    placeholder="Ask anything..."

                />

                <button

                    onClick={handleSend}

                >

                    {
                        loading
                        ?
                        "Sending..."
                        :
                        "Send"
                    }

                </button>

            </div>

        </div>

    );

}

export default Chat;