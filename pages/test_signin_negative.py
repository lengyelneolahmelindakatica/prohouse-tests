import allure
from selenium.common import TimeoutException
from generate_driver import get_preconfigured_chrome_driver
from main_page import MainPage
from SignIn import SignIn

@allure.feature("Belépés")
@allure.story("Sikertelen belépés ellenőrzése")
@allure.severity(allure.severity_level.CRITICAL)
class TestSignIn:
    def setup_method(self):
        self.driver = get_preconfigured_chrome_driver()
        self.main_page = MainPage(self.driver)
        self.signin = SignIn(self.driver)
        self.main_page.browser.set_window_size(1024, 768)
        # Oldal megnyitása
        self.main_page.get()

    def teardown_method(self):
        self.main_page.quit()

    def test_negative_email(self):
        self.main_page.sign_in_button().click()
        self.signin.input_email().send_keys('ilyennincs@enotj.com')
        self.signin.input_password().send_keys('Valid2Password!')
        self.signin.button_signin().click()
        assert self.signin.login_error_message().is_displayed()

    def test_negative_password(self):
        self.main_page.sign_in_button().click()
        self.signin.input_email().send_keys('neapmouxogpgtjksdd@enotj.com')
        self.signin.input_password().send_keys('ezrossz!')
        self.signin.button_signin().click()
        assert self.signin.login_error_message().is_displayed()