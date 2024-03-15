from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):

    EMAIL_FIELD = (By.CSS_SELECTOR, '[id="email-2"]')
    PSW_FIELD = (By.CSS_SELECTOR, '[id="field"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class*="login-button"]')

    def open_login_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def login_to_site(self):
        self.input_text('madimorrison92@gmail.com', *self.EMAIL_FIELD)
        self.input_text('qwerty1234', *self.PSW_FIELD)
        self.click(*self.LOGIN_BUTTON)