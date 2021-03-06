import allure

from config import conf_obj
from src.page import CustomPage


class LoginPage:
    __EMAIL_INPUT: str = '[aria-label="Text\\ field\\ for\\ the\\ login\\ email"]'
    __HAS_TEXT_EMAIL: str = '#login-form div:has-text("Email *")'
    __HAS_TEXT_PASSWORD: str = (
        '[aria-label="Text\\ field\\ for\\ the\\ login\\ password"]'
    )
    __LOGIN_BUTTON: str = '[aria-label="Login"]'
    __LOGIN_MENU_ITEM: str = 'button[role="menuitem"]:has-text("exit_to_app Login")'
    __PASSWORD_INPUT: str = '[aria-label="Text\\ field\\ for\\ the\\ login\\ password"]'
    __SHOW_ACCOUNT_MENU: str = '[aria-label="Show\\/hide\\ account\\ menu"]'
    __WELCOME_BANNER: str = '[aria-label="Close\\ Welcome\\ Banner"]'
    __COOKIE_BANNER: str = "text=Me want it!"

    def __init__(self, page) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.page: CustomPage = page

    @allure.step
    def navigate_to_homepage(self):
        # Go to https://juice-shop.herokuapp.com/login
        self.page.set_window()
        # Click [aria-label="Close\ Welcome\ Banner"]
        if self.page.get_element(self.__COOKIE_BANNER).is_visible():
            self.page.get_element(self.__COOKIE_BANNER).click()

        if self.page.get_element(self.__WELCOME_BANNER).is_visible():
            self.page.get_element(self.__WELCOME_BANNER).click()

    @allure.step
    def login_to_application(self, username, password):
        # Click [aria-label="Show\/hide\ account\ menu"]
        self.page.get_element(self.__SHOW_ACCOUNT_MENU).click()
        # Click button[role="menuitem"]:has-text("exit_to_app Login")
        self.page.get_element(self.__LOGIN_MENU_ITEM).click()
        assert (
            self.page.original.url
            == conf_obj.GLOBAL_URL + "/login#" + conf_obj.LOGIN_URL
        )
        # Click #login-form div:has-text("Email *") >> nth=2
        self.page.get_element(self.__HAS_TEXT_EMAIL).nth(2).click()
        # Fill [aria-label="Text\ field\ for\ the\ login\ email"]
        self.page.get_element(self.__EMAIL_INPUT).fill(username)
        # Click [aria-label="Text\ field\ for\ the\ login\ password"]
        self.page.get_element(self.__HAS_TEXT_PASSWORD).click()
        # Fill [aria-label="Text\ field\ for\ the\ login\ password"]
        self.page.get_element(self.__PASSWORD_INPUT).fill(password)
        # Click [aria-label="Login"]
        self.page.get_element(self.__LOGIN_BUTTON).click()
