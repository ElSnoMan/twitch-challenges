from selenium.webdriver.common.keys import Keys

from google.pages.search import SearchPage


def test_google_search(py):
    py.visit('https://google.com')
    py.get('[name="q"]').type('puppies', Keys.ENTER)
    assert py.should().contain_title('puppies')


def test_google_search_pom(py):
    results_page = SearchPage(py).visit('109.32.407').search('puppies')
    assert 'puppies' in results_page.title()
