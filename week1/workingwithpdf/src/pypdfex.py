from pypdf import PdfReader 


# Open the PDF file
reader = PdfReader("data/Nametable.pdf")

page = reader.pages[0]

text = page.extract_text()

print(text)