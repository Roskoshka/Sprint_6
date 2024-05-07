import allure
import pytest

from data import TestData
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import driver

class TestMainPageFaq:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления нужного текста при нажатии на каждую иконку развертывания в разделе')
    @pytest.mark.parametrize("question, answer, expected_answer",
        [
            (
                MainPageLocators.QUESTION_1,
                MainPageLocators.ANSWER_1,
                TestData.EXPECTED_ANSWER_1,
            ),
            (
                MainPageLocators.QUESTION_2,
                MainPageLocators.ANSWER_2,
                TestData.EXPECTED_ANSWER_2,
            ),
            (
                MainPageLocators.QUESTION_3,
                MainPageLocators.ANSWER_3,
                TestData.EXPECTED_ANSWER_3,
            ),
            (
                MainPageLocators.QUESTION_4,
                MainPageLocators.ANSWER_4,
                TestData.EXPECTED_ANSWER_4,
            ),
            (
                MainPageLocators.QUESTION_5,
                MainPageLocators.ANSWER_5,
                TestData.EXPECTED_ANSWER_5,
            ),
            (
                MainPageLocators.QUESTION_6,
                MainPageLocators.ANSWER_6,
                TestData.EXPECTED_ANSWER_6,
            ),
            (
                MainPageLocators.QUESTION_7,
                MainPageLocators.ANSWER_7,
                TestData.EXPECTED_ANSWER_7,
            ),
            (
                MainPageLocators.QUESTION_8,
                MainPageLocators.ANSWER_8,
                TestData.EXPECTED_ANSWER_8,
            ),
        ])
    def test_click_faq_expand_icons_text_is_expected(self, driver, question, answer, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_element(question)
        main_page.click_on_element(question)
        main_page.wait_visibility_of_element(answer)
        assert main_page.get_text_on_element(answer) == expected_answer
