from pylenium import Pylenium
from selenium.webdriver.common.keys import Keys

from google.pages.results import ResultsPage


class SearchPage:
    def __init__(self, py: Pylenium):
        self.py = py

    # SELECTORS #
    SEARCH_FIELD = '[name="q"]'

    # ACTIONS #

    def visit(self, env) -> 'SearchPage':
        self.py.visit(f'https://{env}.google.com')
        return self

    def search(self, query) -> ResultsPage:
        self.py.get(self.SEARCH_FIELD).type(query, Keys.ENTER)
        return ResultsPage(self.py)
