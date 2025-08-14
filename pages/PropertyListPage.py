from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class PropertyListPage(object):
    def __init__(self):
        self.URL = "http://localhost:4200/property-list;saleType=buy"
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('lang=en')
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 5)

#ha el akarunk navigálni az oldalra
    def get(self):
        self.browser.get(self.URL)

    def quit(self):
        self.browser.quit()
