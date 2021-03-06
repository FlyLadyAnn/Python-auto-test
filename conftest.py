import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


# добавлены две опции - имя браузера (Chrome, FireFox) и язык в браузере(en, ru, es, fr ...)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


# тест в терминале можно запустить:
# - с указанием только браузера, язык будет выбранный установленный по-умолчанию пользователем:
#   pytest --browser_name=chrome test_items.py
# - с указанием браузера и языка:
#   pytest --language=es --browser_name=chrome test_items.py
#
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        if user_language is not None:
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': f'{user_language}'})
            browser = webdriver.Chrome(options=options)
        else:
            browser = webdriver.Chrome()

        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        if user_language is not None:
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", f'{user_language}')
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            browser = webdriver.Firefox()

        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    # now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # browser.get_screenshot_as_file(f"reports/scr_{now}.png")  # скрин
    print("\nquit browser..")
    browser.quit()
