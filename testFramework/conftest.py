import time
import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    # executable_path="D:\\Python Practice\\chromedriver-win64\\chromedriver.exe"
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    #time.sleep(10)
    request.cls.driver = driver
    yield
    driver.close()