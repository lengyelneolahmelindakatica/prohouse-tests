from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.GeneralPage import GeneralPage

class PropertyFormPage(GeneralPage):
    def __init__(self):
        self.URL = 'http://localhost:4200/property-form'
        super().__init__(self.URL)

    def button_facts(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'button1')))

    def button_location(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'button2')))

    def button_features(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'button3')))

