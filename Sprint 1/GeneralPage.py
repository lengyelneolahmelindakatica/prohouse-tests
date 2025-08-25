from generate_driver import get_preconfigured_chrome_driver

class GeneralPage(object):
    def __init__(self, url, browser=None):
        self.URL = url
        if browser is None:
            self.browser = get_preconfigured_chrome_driver()
        else:
            self.browser = browser

    def get(self):
        self.browser.get(self.URL)

    def get_current_url(self):
        return self.browser.current_url

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()
