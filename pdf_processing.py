import PyPDF2
import io

def extract_text_from_pdf(uploaded_file):
    # Read the uploaded PDF file
    pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(uploaded_file.read()))
    text = ""
    
    # Extract text from each page
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    
    return text