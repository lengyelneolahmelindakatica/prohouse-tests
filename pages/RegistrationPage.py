from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from GeneralPage import GeneralPage

class RegistrationPage(GeneralPage):
    def __init__(self, browser=None):
        self.URL = 'http://localhost:4200/registration-form'
        super().__init__(self.URL, browser)

    def last_name_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "lastName")))

    def first_name_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "firstName")))

    def phone_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, "phoneNumber")))

    def email_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form-group']//label[normalize-space(text())='Email address:']/following-sibling::input")))

    def email_confirm_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form-group'][.//label[normalize-space(text())='Email address again:']]//input[@formcontrolname='confirmEmail']")))

    def password_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Please enter a password:']/following-sibling::input")))

    def password_confirm_input(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='confirmPassword']")))

    def register_button(self):
        elem = WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((
            By.XPATH, "//button[@type='submit' and normalize-space(text())='Register']")))
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        return elem

    def email_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']/following-sibling::small[@class='text-danger']")))

    def email_again_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='confirmEmail']/following-sibling::small[@class='text-danger']")))

    def password_field_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']/following-sibling::small[@class='text-danger']")))

    def password_again_field_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='confirmPassword']/following-sibling::small[@class='text-danger']")))

    def last_name_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']/following-sibling::small[@class='text-danger']")))

    def first_name_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']/following-sibling::small[@class='text-danger']")))

    def phone_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='phoneNumber']/following-sibling::small[@class='text-danger']")))

    def fill_registration_form(self, lastname, firstname, phone, email, same_email, password, same_password):
        self.last_name_input().send_keys(lastname)
        self.first_name_input().send_keys(firstname)
        self.phone_input().send_keys(phone)
        self.email_input().send_keys(email)
        self.email_confirm_input().send_keys(same_email)
        self.password_input().send_keys(password)
        self.password_confirm_input().send_keys(same_password)
        self.register_button().click()

