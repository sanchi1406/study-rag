from backend.app.services.parser import extract_pdf_text

text = extract_pdf_text("C:\\Users\\hp\\Desktop\\rag\\backend\\uploads\\abc.pdf")

print("Length:", len(text))
print("--------------------------------")
print(text)
print("--------------------------------")