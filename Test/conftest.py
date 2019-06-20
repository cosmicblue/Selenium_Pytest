import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("C:\\Jar Files\\Driver\\chromedriver.exe") #if not added in PATH
    driver.get("https://localhost:44338/#/maincomponents/home")
    #driver.get("http://seleniumeasy.com/test")
    time.sleep(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()