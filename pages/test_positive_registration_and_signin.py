import allure
import time
import random
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Regisztráció és belépés")
@allure.story("Sikeres regisztráció és belépés ellenőrzése")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.tag("registration")
class TestRegistrationPage:
    def test_positive_registration_and_signin(self, main_page, registration_page, signin_page, base_url):
        # Egyedi email és jelszó generálása
        email = f"user_{int(time.time())}_{random.randint(1000, 9999)}@invalid.com"
        password = "Valid2Password!"

        # Regisztráció
        main_page.registration_button().click()
        assert registration_page.get_current_url() == f"{base_url}/registration-form"

        registration_page.last_name_input().send_keys('Ez')
        registration_page.first_name_input().send_keys('Egy')
        registration_page.phone_input().send_keys('1234')
        registration_page.email_input().send_keys(email)
        registration_page.email_confirm_input().send_keys(email)
        registration_page.password_input().send_keys(password)
        registration_page.password_confirm_input().send_keys(password)

        # Kis várakozás, hogy biztosan minden be legyen töltve
        time.sleep(1)

        # Register gomb kattintás - már van scrollIntoView a Page Object-ben
        register_btn = registration_page.register_button()

        # Extra biztonsági lépés: várunk, hogy kattintható legyen
        WebDriverWait(registration_page.browser, 10).until(EC.element_to_be_clickable(register_btn))

        # JavaScript click alternatív megoldás ha még mindig problémás
        registration_page.browser.execute_script("arguments[0].click();", register_btn)

        # Belépés az új regisztrációval
        signin_page.input_email().send_keys(email)
        signin_page.input_password().send_keys(password)
        signin_page.button_signin().click()

        try:
            # Megpróbálja megtalálni a hibaüzenetet
            assert not signin_page.login_error_message().is_displayed(), "Hibaüzenet jelent meg!"
        except TimeoutException:
            # Nincs hibaüzenet - ez a jó eset
            pass