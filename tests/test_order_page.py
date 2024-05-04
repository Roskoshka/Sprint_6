import allure
import pytest
from conftest import driver
from pages.order_page import OrderPage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data import *


class TestOrderPageOrder:

    @allure.title('Проверка флоу позитивного сценария оформления заказа')
    @allure.description('Тест-сьют на сквозное тестирование функциональности оформления заказа из двух точек входа')
    @pytest.mark.parametrize('button, test_data', [(BasePageLocators.ORDER_BUTTON_IN_HEADER, TestData.test_data1),
                                                   (MainPageLocators.ORDER_BUTTON_IN_MAIN, TestData.test_data2)])
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_display_of_element(OrderPageLocators.BUTTON_CHECK_STATUS_OF_ORDER)
