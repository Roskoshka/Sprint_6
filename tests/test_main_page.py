import allure

from data import TestData
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import driver

class TestMainPageFaq:

    @allure.title('Раздел "Вопросы о важном" - Вопрос 1')
    @allure.description('При клике на вопрос 1 получчаем ответ 1')
    def test_click_faq_question_1_text_is_expected_answer_1(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_1)
        main_page.click_on_element(MainPageLocators.question_1)
        main_page.wait_visibility_of_element(MainPageLocators.answer_1)
        assert main_page.get_text_on_element(MainPageLocators.answer_1) == TestData.expected_answer_1

    @allure.title('Раздел "Вопросы о важном" - Вопрос 2')
    @allure.description('При клике на вопрос 2 получчаем ответ 2')
    def test_click_faq_question_2_text_is_expected_answer_2(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_2)
        main_page.click_on_element(MainPageLocators.question_2)
        main_page.wait_visibility_of_element(MainPageLocators.answer_2)
        assert main_page.get_text_on_element(MainPageLocators.answer_2) == TestData.expected_answer_2

    @allure.title('Раздел "Вопросы о важном" - Вопрос 3')
    @allure.description('При клике на вопрос 3 получчаем ответ 3')
    def test_click_faq_question_3_text_is_expected_answer_3(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_3)
        main_page.click_on_element(MainPageLocators.question_3)
        main_page.wait_visibility_of_element(MainPageLocators.answer_3)
        assert main_page.get_text_on_element(MainPageLocators.answer_3) == TestData.expected_answer_3

    @allure.title('Раздел "Вопросы о важном" - Вопрос 4')
    @allure.description('При клике на вопрос 4 получчаем ответ 4')
    def test_click_faq_question_4_text_is_expected_answer_4(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_4)
        main_page.click_on_element(MainPageLocators.question_4)
        main_page.wait_visibility_of_element(MainPageLocators.answer_4)
        assert main_page.get_text_on_element(MainPageLocators.answer_4) == TestData.expected_answer_4

    @allure.title('Раздел "Вопросы о важном" - Вопрос 5')
    @allure.description('При клике на вопрос 5 получчаем ответ 5')
    def test_click_faq_question_5_text_is_expected_answer_5(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_5)
        main_page.click_on_element(MainPageLocators.question_5)
        main_page.wait_visibility_of_element(MainPageLocators.answer_5)
        assert main_page.get_text_on_element(MainPageLocators.answer_5) == TestData.expected_answer_5

    @allure.title('Раздел "Вопросы о важном" - Вопрос 6')
    @allure.description('При клике на вопрос 6 получчаем ответ 6')
    def test_click_faq_question_6_text_is_expected_answer_6(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_6)
        main_page.click_on_element(MainPageLocators.question_6)
        main_page.wait_visibility_of_element(MainPageLocators.answer_6)
        assert main_page.get_text_on_element(MainPageLocators.answer_6) == TestData.expected_answer_6

    @allure.title('Раздел "Вопросы о важном" - Вопрос 7')
    @allure.description('При клике на вопрос 7 получчаем ответ 7')
    def test_click_faq_question_7_text_is_expected_answer_7(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_7)
        main_page.click_on_element(MainPageLocators.question_7)
        main_page.wait_visibility_of_element(MainPageLocators.answer_7)
        assert main_page.get_text_on_element(MainPageLocators.answer_7) == TestData.expected_answer_7

    @allure.title('Раздел "Вопросы о важном" - Вопрос 8')
    @allure.description('При клике на вопрос 8 получчаем ответ 8')
    def test_click_faq_question_8_text_is_expected_answer_8(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.question_8)
        main_page.click_on_element(MainPageLocators.question_8)
        main_page.wait_visibility_of_element(MainPageLocators.answer_8)
        assert main_page.get_text_on_element(MainPageLocators.answer_8) == TestData.expected_answer_8
