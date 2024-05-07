import pytest
import constants as cnst
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers as hlprs


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument(f'--window-size={cnst.WIDTH},{cnst.HEIGHT}')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(cnst.WIDTH, cnst.HEIGHT)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    data = hlprs.create_new_user()
    payload_for_test = {
        "email": data[0],
        "password": data[1],
        "name": data[2]
    }
    yield payload_for_test
    hlprs.delete_user(data[3])
