import pytest
from generate_driver import get_preconfigured_chrome_driver
from main_page import MainPage
from RegistrationPage import RegistrationPage
from SignIn import SignIn


@pytest.fixture(scope="function")
def driver():
    # WebDriver inicializálása a generate_driver.py segítségével
    driver = get_preconfigured_chrome_driver()
    driver.set_window_size(1024, 768)  # Ablakméret beállítása minden teszthez
    yield driver
    # Teszt végeztével bezárjuk a böngészőt
    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    # MainPage objektum inicializálása
    page = MainPage(driver)
    page.get()  # Navigálunk a főoldalra
    return page

@pytest.fixture(scope="function")
def registration_page(driver):
    # RegistrationPage objektum inicializálása
    return RegistrationPage(driver)

@pytest.fixture(scope="function")
def signin_page(driver):
    # SignIn objektum inicializálása
    return SignIn(driver)

@pytest.fixture(scope="session")
def base_url():
    # Közös URL definiálása
    return "http://localhost:4200"