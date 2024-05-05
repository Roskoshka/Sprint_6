import allure

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_on_element(BasePageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Кликнуть по кнопке "Заказать" на странице')
    def click_on_order_button_on_page(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_IN_MAIN)

    @allure.step('Кликнуть по "Самокат" в лого хэдера')
    def click_header_logo_scooter(self):
        self.click_on_element(BasePageLocators.HEADER_LOGO_SCOOTER)

    @allure.step('Кликнуть по "Яндекс" в лого хэдера')
    def click_header_logo_yandex(self):
        self.click_on_element(BasePageLocators.HEADER_LOGO_YANDEX)
