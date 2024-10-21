import time
import pytest
from selenium import webdriver
Driver = None

@pytest.fixture(autouse=True)
def setup(request):
    global driver

    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("headless")
    driver = webdriver.Chrome()
    # executable_path="D:\\Python Practice\\chromedriver-win64\\chromedriver.exe"
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    #time.sleep(10)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)