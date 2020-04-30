from pylenium import Pylenium
from selenium.webdriver.common.keys import Keys

from copart_com.pages.results import ResultsPage


class HomePage:
    def __init__(self, py: Pylenium):
        self.py = py

    # SELECTOR #

    SEARCH_FIELD = '#input-search'

    @property
    def SEARCH_BUTTON(self):
        """ Use this with py.contains(). """
        return 'Search'

    # ACTIONS #

    def visit(self) -> 'HomePage':
        self.py.visit('https://copart.com')
        return self

    def search(self, query) -> ResultsPage:
        self.py.get(self.SEARCH_FIELD).type(query)
        self.py.contains(self.SEARCH_BUTTON).click()
        return ResultsPage(self.py)
