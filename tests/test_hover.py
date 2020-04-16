from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_hover(py):
    py.visit('https://qap.dev')
    py.get("[href='/about']").hover()


def test_hover_with_selenium():
    driver = webdriver.Chrome()
    driver.get('https://qap.dev')
    element = driver.find_element(By.CSS_SELECTOR, "[href='/about']")
    ActionChains(driver).move_to_element(element).perform()
