import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaCloudUploadAlt } from "react-icons/fa";
import api from "../services/api";

function UploadSection() {

    const navigate = useNavigate();

    const [files, setFiles] = useState([]);
    const [website, setWebsite] = useState("");
    const [youtube, setYoutube] = useState("");
    const [loading, setLoading] = useState(false);

    const handleUpload = async () => {

        try {

            setLoading(true);

            // Upload Files
            if (files.length > 0) {

                const formData = new FormData();

                files.forEach((file) => {
                    formData.append("files", file);
                });

                await api.post("/upload/files", formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                });

            }

            // Upload Website
            if (website.trim() !== "") {

                await api.post("/upload/source", {
                    source: website,
                });

            }

            // Upload YouTube
            if (youtube.trim() !== "") {

                await api.post("/upload/source", {
                    source: youtube,
                });

            }

            alert("Study Material Uploaded Successfully!");

            navigate("/chat");

        }
        catch (error) {

            console.error(error);

            alert("Upload Failed!");

        }
        finally {

            setLoading(false);

        }

    };

    return (

        <section
            id="upload"
            className="upload-section"
        >

            <h2 className="upload-heading">
                Upload Study Material
            </h2>

            <div className="upload-card">

                <label className="upload-box">

                    <FaCloudUploadAlt
                        className="upload-icon"
                    />

                    <h3>
                        Drag & Drop Files Here
                    </h3>

                    <p>
                        or click to browse
                    </p>

                    <span>
                        PDF • DOCX • PPT • PPTX
                    </span>

                    <input
                        hidden
                        multiple
                        type="file"
                        accept=".pdf,.doc,.docx,.ppt,.pptx"
                        onChange={(e) =>
                            setFiles((prevFiles) => [
                                ...prevFiles,
                                ...Array.from(e.target.files),
                            ])
                        }
                    />

                </label>

                {files.length > 0 && (

                    <div className="selected-files">

                        <h3>Selected Files</h3>

                        {files.map((file, index) => (

                            <div
                                key={index}
                                className="file-item"
                            >

                                <span>
                                    📄 {file.name}
                                </span>

                                <button
                                    className="remove-btn"
                                    onClick={() =>
                                        setFiles(
                                            files.filter(
                                                (_, i) => i !== index
                                            )
                                        )
                                    }
                                >
                                    ✖
                                </button>

                            </div>

                        ))}

                    </div>

                )}

                <input
                    className="input-box"
                    type="text"
                    placeholder="Paste Website URL"
                    value={website}
                    onChange={(e) =>
                        setWebsite(e.target.value)
                    }
                />

                <input
                    className="input-box"
                    type="text"
                    placeholder="Paste YouTube URL"
                    value={youtube}
                    onChange={(e) =>
                        setYoutube(e.target.value)
                    }
                />

                <button
                    className="process-btn"
                    onClick={handleUpload}
                    disabled={loading}
                >

                    {loading
                        ? "Processing..."
                        : "Process Material"}

                </button>

            </div>

        </section>

    );

}

export default UploadSection;