import allure

from main_page import MainPage

class TestMainPage(object):
    def setup_method(self):
        self.page = MainPage()
        self.page.browser.maximize_window()  # Ablak méretezése a teljes képernyőre
        self.page.get()
        print(self.page.browser.get_window_size())  # Ablak méret kiírása (800x600 a maxwindow, nem látszanak az elemek, emiatt törik)
        self.page.browser.set_window_size(1024, 768) # Ablak méretezése 1024x768-ra, hogy minden elem látszódjon


    def teardown_method(self):
        self.page.quit()

    @allure.feature("Smoke teszt")
    @allure.story("Main Page UI ellenőrzés")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("smoke")
    def test_smoke(self):
        assert self.page.page_logo().is_displayed()
        assert self.page.buy_button().is_displayed()
        print(self.page.buy_button().text)# nem jó az xpath

        assert self.page.rent_button().is_displayed()
        assert self.page.sign_in_button().is_displayed()
        assert self.page.registration_button().is_displayed()
        assert self.page.language_switch().is_displayed()
        assert self.page.search_input().is_displayed()