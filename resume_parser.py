import pdfplumber
import fitz  # PyMuPDF
import io
from PIL import Image


# def extract_text_from_pdf(file):
#     text = ""
    
#     try:
#         with pdfplumber.open(file) as pdf:
#             for page in pdf.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     text += page_text + "\n"
                    
#     except Exception as e:
#         print("Error reading PDF:", e)
    
#     return text

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

def extract_image_from_pdf(file):
    images = []

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                for img in page.images:
                    images.append(img)
    except:
        pass

    return images



def extract_image_from_pdf(file):
    try:
        file.seek(0)  # VERY IMPORTANT

        pdf = fitz.open(stream=file.read(), filetype="pdf")

        for page_index in range(len(pdf)):
            page = pdf[page_index]
            images = page.get_images(full=True)

            if images:
                xref = images[0][0]  # first image
                base_image = pdf.extract_image(xref)
                image_bytes = base_image["image"]

                image = Image.open(io.BytesIO(image_bytes))
                return image

        return None

    except Exception as e:
        print("Image extraction error:", e)
        return None