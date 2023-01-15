import time
from typing import Literal, Callable

import pytest
from selene.support.shared import browser
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from demoqa_tests.utils import attach

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from dotenv import load_dotenv



@pytest.fixture(scope='function', autouse=True) # scope='function' - применять к функциям, autouse=True - автоматическое использование фикстур -не указывать аргумент в тесте
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.timeout = 5.0  # выставление таймаута
    browser.config.window_width = 1360
    browser.config.window_height = 900
    browser.config.hold_browser_open = True

    DEFAULT_BROWSER_VERSION = "100.0"

    def pytest_addoption(parser):
        parser.addoption(
            '--browser_version',
            default='100.0'
        )

    @pytest.fixture(scope='session', autouse=True)
    def load_env():
        load_dotenv()

    @pytest.fixture(scope='function')
    def setup_browser(request):
        browser_version = request.config.getoption('--browser_version')
        browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )
        browser = Browser(Config(driver))

    yield # даст управление тесту - выполняет и возвращает управление назад и где можно сделать какие-то действия  (генератор) - yield - ключевое слово которое позволяет по среди функции вернуть управление навверх туда где эта функция использовалась запросить что-то доп  получить доделать свою работу и вернуть назад
   # time.sleep(5) # билиотека time

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit() # закрытие браузера

