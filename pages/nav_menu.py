from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class NavMenu(Page):

    NAV_MAIN_MENU = (By.CSS_SELECTOR, '.menu-block [href="/"]')
    NAV_SETTINGS = (By.CSS_SELECTOR, '.menu-block [href="/settings"]')

    def click_settings_option(self):
        self.wait_element_visible(*self.NAV_MAIN_MENU)
        self.click(*self.NAV_SETTINGS)