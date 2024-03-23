from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):

    CONTACT_US_BTN = (By.CSS_SELECTOR, '.settings-block-menu [href="/contact-us"]')

    def click_contact_us_button(self):
        sleep(1)
        self.click(*self.CONTACT_US_BTN)