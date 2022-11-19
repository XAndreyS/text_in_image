

import requests
import pytesseract
from PIL import Image
from pytesseract import pytesseract


def capcha_in_text(locator_capcha):
    """Функция принимаеет веб-элемент в качестве  аргумента, затем получчает атрибут src, в котором хранится
    url капчи"""
    img_save = requests.get(locator_capcha.get_attribute('src'))
    out = open(f"image\capcha_new.png", "wb")
    out.write(img_save.content)
    out.close()
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open("image\capcha_new.png")
    # получаем строку
    string = pytesseract.image_to_string(img, lang="eng",
                                         config='--psm 6 -c tessedit_char_whitelist=0123456789')
    return string


