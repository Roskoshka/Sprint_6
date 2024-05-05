import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import *


class OrderPage(BasePage):

    @allure.step('Кликнуть по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.SELECT_ITEM_IN_DROPDOWN_METRO)

    @allure.step('Кликнуть по выбранной дате в выпадающем календаре поля ввода даты начала аренды')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.CALENDAR_ITEM)

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.INPUT_NAME)
        self.click_on_element(OrderPageLocators.INPUT_NAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_NAME, test_data[0])
        self.click_on_element(OrderPageLocators.INPUT_LASTNAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_LASTNAME, test_data[1])
        self.click_on_element(OrderPageLocators.INPUT_ADDRESS)
        self.send_keys_to_input(OrderPageLocators.INPUT_ADDRESS, test_data[2])
        self.click_on_element(OrderPageLocators.INPUT_METRO)
        self.send_keys_to_input(OrderPageLocators.INPUT_METRO, test_data[3])
        self.click_on_element(OrderPageLocators.SELECT_ITEM_IN_DROPDOWN_METRO)
        self.click_on_element(OrderPageLocators.INPUT_PHONE)
        self.send_keys_to_input(OrderPageLocators.INPUT_PHONE, test_data[4])
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.INPUT_DATE)
        self.click_on_element(OrderPageLocators.INPUT_DATE)
        self.send_keys_to_input(OrderPageLocators.INPUT_DATE, test_data[5])
        self.click_on_element(OrderPageLocators.CHECKBOX_GREY_COLOR_SCOOTER)
        self.click_on_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.INPUT_COMMENT)
        self.send_keys_to_input(OrderPageLocators.INPUT_COMMENT, test_data[6])
        self.click_on_element(OrderPageLocators.BUTTON_MAKE_ORDER)
        self.wait_visibility_of_element(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)
        self.click_on_element(OrderPageLocators.BUTTON_YES_CONFIRM_ORDER)

    @allure.step('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа - статус заказа виден.')
    def check_display_status_of_order(self):
        self.check_display_of_element(OrderPageLocators.BUTTON_CHECK_STATUS_OF_ORDER)