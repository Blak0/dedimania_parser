from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


driver = None


def init_driver():
    global driver
    if not driver:

        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)
    return driver
