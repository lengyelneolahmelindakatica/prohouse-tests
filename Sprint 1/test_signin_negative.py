import allure


@allure.feature("Belépés")
@allure.story("Sikertelen belépés ellenőrzése")
@allure.severity(allure.severity_level.CRITICAL)
class TestSignIn:
    def test_negative_email(self, main_page, signin_page):
        main_page.sign_in_button().click()
        signin_page.input_email().send_keys('ilyennincs@enotj.com')
        signin_page.input_password().send_keys('Valid2Password!')
        signin_page.button_signin().click()
        assert signin_page.login_error_message().is_displayed()

    def test_negative_password(self, main_page, signin_page):
        main_page.sign_in_button().click()
        signin_page.input_email().send_keys('neapmouxogpgtjksdd@enotj.com')
        signin_page.input_password().send_keys('ezrossz!')
        signin_page.button_signin().click()
        assert signin_page.login_error_message().is_displayed()