from pypdf import PdfReader
from text_processor import clean_text

def read_pdf(path):
    reader = PdfReader(path)

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        
        if text:
            full_text += text + "\n"

    return clean_text(full_text)


if __name__ == "__main__":
    text = read_pdf("document.pdf")

    print(text)
