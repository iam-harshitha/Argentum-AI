# loader.py
import pdfplumber
import os

def load_and_chunk_pdf(file_path, chunk_size=500):
    """
    Load a PDF and split its text into chunks.
    :param file_path: Path to PDF
    :param chunk_size: Max characters per chunk
    :return: List of text chunks
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] File does not exist: {file_path}")
        return []

    try:
        print(f"[INFO] Loading PDF from: {file_path}")
        full_text = ""

        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
                else:
                    print(f"[WARN] Page {i+1} has no extractable text.")

        if not full_text.strip():
            print("[X] No extractable text found in the PDF.")
            return []

        # Split into chunks manually
        chunks = []
        for i in range(0, len(full_text), chunk_size):
            chunks.append(full_text[i:i + chunk_size])

        print(f"[INFO] Document loaded and split into {len(chunks)} chunks.")
        return chunks

    except Exception as e:
        print(f"[ERROR] Failed to process PDF: {e}")
        return []
