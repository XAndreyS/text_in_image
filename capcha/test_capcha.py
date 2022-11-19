"""Пример работы функции по чтению текста с картинки из файла capcha.py"""

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from capcha import capcha_in_text




def test_capcha():
    """Проверяем код,для чтения картинки"""

    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    # Переходим на страницу восстановления пароля
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?')
    time.sleep(10)  # мой ПК не всегда успевает загружать страницу

    image_capcha = driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')  # локатор капчи
    capcha_input = driver.find_element(By.XPATH, '//input[@id="captcha"]')  # Локатор поля ввода капчи

    # Вызываем функцию capcha_in_text, передаем в качестве аргумента веб-элемент капчи(картинки)
    # исохраняем в переменную capcha_text
    capcha_text = capcha_in_text(image_capcha)
    capcha_input.clear()
    capcha_input.send_keys(capcha_text)  # Вводим результат(переменную с текстом капчи) в поле ввода

    time.sleep(2) # слип,что бы успеть помотреть,что он ввел, вы это будете проверять с помощью assert
    # Сохранить текст  картинки в файл txt для наглядности работы функции(напомню, она периодически ошибается)
    with open("namefile1.txt", 'a', encoding="utf=8") as myFile:
        print(f'{capcha_text}', file=myFile)
    driver.quit()

test_capcha()