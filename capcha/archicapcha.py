

import requests
import pytesseract
from PIL import Image
from pytesseract import pytesseract
import io
import os

class ArchiCapcha():

    def capcha_in_text(Web_element):
        """Функция принимаеет веб-элемент в качестве  аргумента, затем получчает атрибут src, в котором хранится
        url капчи"""
        img_save = requests.get(Web_element.get_attribute('src')).content
        #with open(f"image\capcha_new.png", "wb") as file:
        #    file.write(img_save.content)

        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        img = Image.open(io.BytesIO(img_save))
        #img = Image.open('image\capcha_new.png')
        # получаем строку
        string = pytesseract.image_to_string(img, lang="eng",
                                             config='--psm 6 -c tessedit_char_whitelist=0123456789')
        #os.remove('image\capcha_new.png')
        return string



