import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def set_config():
    browser.config.timeout = 15
    browser.config.window_width = 1080
    browser.config.window_height = 920
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()
