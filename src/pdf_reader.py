from pypdf import PdfReader

def read_pdf(path):
    reader = PdfReader(path)

    for page in reader.pages:
        text = page.extract_text()
        print(text)


if __name__ == "__main__":
    read_pdf("document.pdf")
