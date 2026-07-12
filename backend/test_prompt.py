from app.prompts.rag_prompt import RAG_PROMPT

context = """
A simple graph is an undirected graph having no self-loops
and no multiple edges.
"""

question = "What is a simple graph?"

prompt = RAG_PROMPT.format(
    context=context,
    question=question
)

print(prompt)