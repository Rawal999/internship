import fitz  # PyMuPDF

doc = fitz.open("data/Nametable.pdf")
page = doc[0]

# For tables
tables = page.find_tables()
if tables:
    table = tables[0]
    print(table.extract())