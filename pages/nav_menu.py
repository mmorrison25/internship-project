from selenium.webdriver.common.by import By
from pages.base_page import Page


class NavMenu(Page):

    NAV_MAIN_MENU = (By.CSS_SELECTOR, 'a[href="/"] [class*="menu-button"]')
    NAV_SETTINGS = (By.CSS_SELECTOR, 'a[href="/settings"] [class*="menu-button"]')

    def click_settings_option(self):
        self.wait_element_visible(*self.NAV_MAIN_MENU)
        self.click(*self.NAV_SETTINGS)