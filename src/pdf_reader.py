from PyPDF2 import PdfReader

def read_pdf(file_path):
    # Create a PDF reader object
    reader = PdfReader(file_path)
    
    # Get the number of pages
    num_pages = len(reader.pages)
    print(f"\nTotal number of pages: {num_pages}")
    
    # Extract text from all pages
    text = ""
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += f"\n--- Page {page_num + 1} ---\n"
        text += page.extract_text()
    
    return text

if __name__ == "__main__":
    pdf_path = "Yara_Turetsky_20x52x9_4_12_roof_Ukrainian_Refugee_Housing_MA.pdf"
    content = read_pdf(pdf_path)
    print(content) 