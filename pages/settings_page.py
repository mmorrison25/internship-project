from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):

    CONTACT_US_BTN = (By.CSS_SELECTOR, 'a[href="/contact-us"] [class="setting-text"]')

    def click_contact_us_button(self):
        self.click(*self.CONTACT_US_BTN)