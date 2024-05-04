import allure
from conftest import driver
from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators


class TestRedirectLogo:
    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат" в шапке')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_element(MainPageLocators.ORDER_BUTTON_IN_MAIN)
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_element(BasePageLocators.HEADER_LOGO_SCOOTER)
        main_page.click_header_logo_scooter()
        assert main_page.check_display_of_element(MainPageLocators.MAIN_HEADER)

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_element(BasePageLocators.HEADER_LOGO_YANDEX)
        main_page.click_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert main_page.get_page_title(BasePageLocators.TITLE) == 'Дзен'