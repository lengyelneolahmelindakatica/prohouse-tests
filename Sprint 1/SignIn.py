from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from GeneralPage import GeneralPage

class SignIn(GeneralPage):
    def __init__(self, browser=None):
        self.URL = 'http://localhost:4200'
        super().__init__(self.URL, browser)

    def input_email(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "email")))

    def input_password(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "password")))

    def button_signin(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Sign in']")))

    def link_registration(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-center']//a[@routerlink='/registration-form']")))

    def login_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']/following-sibling::small[@class='text-danger']")))

    def fill_form_signin(self, email, password):
        self.input_email().send_keys(email)
        self.input_password().send_keys(password)
        self.button_signin().click()

    def new_registration(self):
        self.link_registration().click()