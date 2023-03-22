import pytest
from selenium import webdriver
driver=None

from config.config import *
@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome(executable_path="C:\\temp\\chromedriver_win32 (9)\\chromedriver.exe")
    driver.maximize_window()
    driver.get(app_url)
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.quit()