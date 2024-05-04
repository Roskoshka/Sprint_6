from selenium.webdriver.common.by import By


class MainPageLocators:

    # Заголовок "Самокат на пару дней"
    MAIN_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')

    # Кнопка "Заказать" на главной странице
    ORDER_BUTTON_IN_MAIN = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')

    # Раздел "Вопросы о важном"
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")

    # Вопросы:
    # Вопрос 1: "Сколько это стоит? И как оплатить?"
    question_1 = (By.XPATH, "//div[@id='accordion__heading-0']/parent::div")
    # Вопрос 2: "Хочу сразу несколько самокатов! Так можно?"
    question_2 = (By.XPATH, "//div[@id='accordion__heading-1']/parent::div")
    # Вопрос 3: "Как рассчитывается время аренды?"
    question_3 = (By.XPATH, "//div[@id='accordion__heading-2']/parent::div")
    # Вопрос 4: "Можно ли заказать самокат прямо на сегодня?"
    question_4 = (By.XPATH, "//div[@id='accordion__heading-3']/parent::div")
    # Вопрос 5: "Можно ли продлить заказ или вернуть самокат раньше?"
    question_5 = (By.XPATH, "//div[@id='accordion__heading-4']/parent::div")
    # Вопрос 6: "Вы привозите зарядку вместе с самокатом?"
    question_6 = (By.XPATH, "//div[@id='accordion__heading-5']/parent::div")
    # Вопрос 7: "Можно ли отменить заказ?"
    question_7 = (By.XPATH, "//div[@id='accordion__heading-6']/parent::div")
    # Вопрос 8: "Я жизу за МКАДом, привезёте?"
    question_8 = (By.XPATH, "//div[@id='accordion__heading-7']/parent::div")

    # Ответы:
    # Ответ 1
    answer_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
    # Ответ 2
    answer_2 = (By.XPATH, "//div[@id='accordion__panel-1']")
    # Ответ 3
    answer_3 = (By.XPATH, "//div[@id='accordion__panel-2']")
    # Ответ 4
    answer_4 = (By.XPATH, "//div[@id='accordion__panel-3']")
    # Ответ 5
    answer_5 = (By.XPATH, "//div[@id='accordion__panel-4']")
    # Ответ 6
    answer_6 = (By.XPATH, "//div[@id='accordion__panel-5']")
    # Ответ 7
    answer_7 = (By.XPATH, "//div[@id='accordion__panel-6']")
    # Ответ 8
    answer_8 = (By.XPATH, "//div[@id='accordion__panel-7']")