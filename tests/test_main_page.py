import allure
import pytest

from data import TestData
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import driver

class TestMainPageFaq:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления нужного текста при нажатии на каждую иконку развертывания в разделе')
    @pytest.mark.parametrize("question_number, expected_answer", TestData.test_data_answers_faq_section)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.FAQ_SECTION)
        main_page.wait_visibility_of_element(MainPageLocators.FAQ_QUESTIONS_ITEMS[question_number])
        main_page.click_on_element(MainPageLocators.FAQ_QUESTIONS_ITEMS[question_number])
        main_page.wait_visibility_of_element(MainPageLocators.FAQ_ANSWERS_ITEMS[question_number])
        assert main_page.get_text_on_element(MainPageLocators.FAQ_ANSWERS_ITEMS[question_number]) == expected_answer
