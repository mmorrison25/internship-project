from selenium.webdriver.common.by import By
from pages.base_page import Page


class ContactPage(Page):

    SOCIAL_MEDIA_ICON = (By.CSS_SELECTOR, '[class*="social-button"]')

    def verify_social_media_icons(self):
        self.find_elements(*self.SOCIAL_MEDIA_ICON)