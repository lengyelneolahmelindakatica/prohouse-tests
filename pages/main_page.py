from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GeneralPage import GeneralPage

class MainPage(GeneralPage):
    def __init__(self, browser=None):
        self.URL = 'http://localhost:4200'
        super().__init__(self.URL, browser)

    def page_logo(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='brand']")))

    def buy_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Buy']")))

    def rent_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Rent']")))

    def sign_in_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Sign In']")))

    def registration_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Registration']")))

    def search_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "geoapify-autocomplete-input")))

    def language_switch(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//app-nav[@class='navlink language-selector']")))

    def button_my_properties(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/my-property-list']")))