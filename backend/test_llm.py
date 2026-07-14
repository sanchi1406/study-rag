from app.services.llm import generate_answer

context = """
A simple graph is an undirected graph having no self-loops
and no multiple edges.
"""

question = "What is a simple graph?"

answer = generate_answer(
    question=question,
    context=context
)

print(answer)