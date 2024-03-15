from pages.base_page import Page
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.nav_menu import NavMenu
from pages.settings_page import SettingsPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.contact_page = ContactPage(driver)
        self.login_page = LoginPage(driver)
        self.nav_menu = NavMenu(driver)
        self.settings_page = SettingsPage(driver)