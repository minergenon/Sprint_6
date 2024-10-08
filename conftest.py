import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import MAIN_PAGE

@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()
