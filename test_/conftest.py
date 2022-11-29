import pytest
from library.config import Config
from selenium import webdriver


@pytest.fixture(params=["Edge","Chrome",])
def _driver(request):




    if request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_path)



    elif request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_path)



    driver.get(Config.url)
    driver.maximize_window()
    driver.implicitly_wait(50)
    yield driver
    print(driver.title)
    # driver.save_screenshot("text_loginpage.png")
    driver.close()

