import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_button_is_located(browser):
    # Ссылка на страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # Открываем страницу товара
    browser.get(link)

    # Смотрим, что страница запустилась с необходимым языком
    time.sleep(30)

    try:
        # Ожидание, пока кнопка добавления в корзину станет доступной
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
        
        # Проверка с помощью assert, что кнопка добавления в корзину присутствует
        assert add_to_cart_button, "Кнопка добавления в корзину не найдена на странице товара"
    
    except Exception as e:
        # В случае, если элемент не найден, выбрасываем исключение с сообщением об ошибке
        pytest.fail(f"Тест не пройден: {e}")
