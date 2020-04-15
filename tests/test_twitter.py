import os

from selenium.webdriver.common.keys import Keys


def test_twitter_like(py):
    py.visit('https://twitter.com')
    py.get("[name='session[username_or_email]']").type('carlos.e.kidman@gmail.com')
    py.get("[name='session[password]']").type(os.getenv('TWITTER_PASSWORD'))
    py.get("[data-testid='LoginForm_Login_Button']").click()
    py.get("[data-testid='SearchBox_Search_Input']").type('#testautomation', Keys.ENTER)
    py.get("[data-testid='like']").click()
    py.screenshot('liked_it_brah.png')
