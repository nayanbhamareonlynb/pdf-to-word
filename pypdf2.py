#pip install pypdf2

# Create a Python script to extract data from PDF.
import PyPDF2

FILE_PATH = 'filename.pdf'

with open(FILE_PATH, mode='rb') as f:

    reader = PyPDF2.PdfFileReader(f)

    page = reader.getPage(0)

    print(page.extractText())

    # Run the script to extract data from PDF to Word.
    # pypdf2.py > filename.doc