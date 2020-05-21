import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Safari()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=10)


def test_safari_stuff(driver, wait):
    driver.get('https://google.com')
    driver.find_element_by_name('q').send_keys('puppies', Keys.ENTER)
    assert wait.until(lambda x: 'puppies' in x.title)


def test_qap_with_safari(driver, wait):
    driver.get('https://qap.dev')
    driver.find_element(By.CSS_SELECTOR, 'a[href="/about"]').click()
    pass