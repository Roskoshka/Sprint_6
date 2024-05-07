from selenium.webdriver.common.by import By


class MainPageLocators:

    # Заголовок "Самокат на пару дней"
    MAIN_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')

    # Кнопка "Заказать" на главной странице
    ORDER_BUTTON_IN_MAIN = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')

    # Раздел "Вопросы о важном"
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")

    # Вопросы раздела "Вопросы о важном":
    QUESTION_1 = (By.XPATH, "//div[@id='accordion__heading-0']/parent::div")
    QUESTION_2 = (By.XPATH, "//div[@id='accordion__heading-1']/parent::div")
    QUESTION_3 = (By.XPATH, "//div[@id='accordion__heading-2']/parent::div")
    QUESTION_4 = (By.XPATH, "//div[@id='accordion__heading-3']/parent::div")
    QUESTION_5 = (By.XPATH, "//div[@id='accordion__heading-4']/parent::div")
    QUESTION_6 = (By.XPATH, "//div[@id='accordion__heading-5']/parent::div")
    QUESTION_7 = (By.XPATH, "//div[@id='accordion__heading-6']/parent::div")
    QUESTION_8 = (By.XPATH, "//div[@id='accordion__heading-7']/parent::div")

    # Ответы раздела "Вопросы о важном":
    ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
    ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-1']")
    ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-2']")
    ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-3']")
    ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-4']")
    ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-5']")
    ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-6']")
    ANSWER_8 = (By.XPATH, "//div[@id='accordion__panel-7']")
