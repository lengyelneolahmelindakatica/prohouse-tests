import allure
import time
import random
from selenium.common import TimeoutException

@allure.feature("Regisztráció és belépés")
@allure.story("Sikeres regisztráció és belépés ellenőrzése")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.tag("registration")
class TestRegistrationPage:
    def test_positive_registration_and_signin(self, main_page, registration_page, signin_page, base_url):
        print("Teszt indul")
        main_page.registration_button().click()
        print("Regisztráció gombra kattintva, URL:", registration_page.get_current_url())