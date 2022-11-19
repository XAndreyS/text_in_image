"""Пример работы функции по чтению текста с картинки из файла capcha.py"""

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from archicapcha import ArchiCapcha


def test_capcha():
    """Проверяем код,для чтения картинки"""

    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    # Переходим на страницу восстановления пароля
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?')
    driver.implicitly_wait(50)

    image_capcha = driver.find_element(By.CSS_SELECTOR, 'img.rt-captcha__image')  # локатор капчи
    capcha_input = driver.find_element(By.CSS_SELECTOR, 'input#captcha')  # Локатор поля ввода капчи
    user_phone = driver.find_element(By.CSS_SELECTOR, 'input#username') # Локатор поля телефона
    button_next = driver.find_element(By.CSS_SELECTOR, 'button#reset')  # Локатор кнопки продолжить
    #text_error = driver.find_element(By.CSS_SELECTOR, 'p.card-container__error')
    # Вызываем функцию capcha_in_text, передаем в качестве аргумента веб-элемент капчи(картинки)
    # исохраняем в переменную capcha_text
    def enter_button():
        capcha_text = ArchiCapcha.capcha_in_text(image_capcha)
        #capcha_input.clear()
        capcha_input.send_keys(capcha_text)# Вводим результат(переменную с текстом капчи) в поле ввода
        #user_phone.clear()
        user_phone.send_keys('9068080311')
        button_next.click()


    for i in range(10):
        enter_button()

        if driver.find_element(By.CSS_SELECTOR, 'p.card-container__error').is_displayed():
            image_capcha = driver.find_element(By.CSS_SELECTOR, 'img.rt-captcha__image')  # локатор капчи
            enter_button()
        else:
            break
    assert 2==2

    driver.quit()

test_capcha()