from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Экран "Для кого самокат"
    TITLE_PAGE_PERSONAL_INFO = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    SELECT_ITEM_IN_DROPDOWN_METRO = (By.XPATH, ".//li[@class='select-search__row']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Экран "Про аренду"
    TITLE_PAGE_RENT_INFO = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.XPATH, "//div[@class='react-datepicker-popper']")
    CALENDAR_ITEM = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    FIELD_RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    DROPDOWN_ITEM_RENTAL_PERIOD = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    CHECKBOX_GREY_COLOR_SCOOTER = (By.XPATH, "//input[@id='grey']")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_MAKE_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Подтверждение заказа
    BUTTON_YES_CONFIRM_ORDER = (By.XPATH, "//button[text()='Да']")
    BUTTON_CHECK_STATUS_OF_ORDER = (By.XPATH, ".//*[text()='Посмотреть статус']")
