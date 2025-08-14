import allure

class TestMainPage(object):
    @allure.feature("Smoke teszt")
    @allure.story("Main Page UI ellenőrzés")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("smoke")
    def test_smoke(self, main_page):
        assert main_page.page_logo().is_displayed()
        assert main_page.buy_button().is_displayed()
        print(main_page.buy_button().text)
        assert main_page.rent_button().is_displayed()
        assert main_page.sign_in_button().is_displayed()
        assert main_page.registration_button().is_displayed()
        assert main_page.language_switch().is_displayed()
        assert main_page.search_input().is_displayed()