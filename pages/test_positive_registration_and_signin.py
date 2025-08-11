import allure
import time
import random
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


from generate_driver import get_preconfigured_chrome_driver
from RegistrationPage import RegistrationPage
from main_page import MainPage
from SignIn import SignIn



class TestRegistrationPage(object):
    def setup_method(self):
        temporary_driver = get_preconfigured_chrome_driver()
        self.reg_page = RegistrationPage(temporary_driver)
        self.page = MainPage(temporary_driver)
        self.signin_page = SignIn(temporary_driver)
        self.page.get()
        print(self.page.browser.get_window_size())  # Ablak méret kiírása (800x600 a maxwindow, nem látszanak az elemek, emiatt törik)
        self.page.browser.set_window_size(1024, 768)  # Ablak méretezése 1024x768-ra, hogy minden elem látszódjon

        # 💡 Itt hozzuk létre az egyedi emailt és jelszót
        self.email = f"user_{int(time.time())}_{random.randint(1000, 9999)}@invalid.com"
        self.password = "Valid2Password!"

    def teardown_method(self):
        self.reg_page.quit()

    @allure.title("ProHouse Registration")
    @allure.description("A regisztráció tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("registration")
    def test_positive_registration_and_signin(self):
        #a főoldalon vagyunk
        self.page.registration_button().click()
        assert self.reg_page.get_current_url() == self.reg_page.URL
        #regisztrációs oldalra navigált
        self.reg_page.last_name_input().send_keys('Ez')
        self.reg_page.first_name_input().send_keys('Egy')
        self.reg_page.phone_input().send_keys('1234')
        self.reg_page.email_input().send_keys(self.email)
        self.reg_page.email_confirm_input().send_keys(self.email)
        self.reg_page.password_input().send_keys(self.password)
        self.reg_page.password_confirm_input().send_keys(self.password)
        self.page.browser.execute_script("arguments[0].click();", self.reg_page.register_button())


        #főoldalra,ott is a rögtön a belépésre vissz,és belépünk az új regisztrációval
        self.signin_page.input_email().send_keys(self.email)
        self.signin_page.input_password().send_keys(self.password)
        self.signin_page.button_signin().click()
        try:
        # Megpróbálja megtalálni a hibaüzenetet
            assert not self.signin_page.login_error_message().is_displayed(), "Hibaüzenet jelent meg!"
        except TimeoutException:
        # Nincs hibaüzenet
            pass