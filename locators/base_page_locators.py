from selenium.webdriver.common.by import By


class BasePageLocators:
    # Лого "Яндекс"
    HEADER_LOGO_SCOOTER = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    # Лого "Самокат"
    HEADER_LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')

    # Кнопка "Заказать" в хедере
    ORDER_BUTTON_IN_HEADER = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    # Заголовок страницы <title>
    TITLE = (By.TAG_NAME, 'title')
