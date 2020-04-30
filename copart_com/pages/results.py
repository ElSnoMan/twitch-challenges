from pylenium import Pylenium


class ResultsPage:
    def __init__(self, py: Pylenium):
        self.py = py

    FILTER_SEARCH_FIELD = "input[type='search']"
    LOADER_SPINNER = '#serverSideDataTable_processing'

    def filter_search(self, query) -> 'ResultsPage':
        self.py.get(self.FILTER_SEARCH_FIELD).type(query)
        # return self.wait_for_results_load()
        return self

    def wait_for_results_load(self) -> 'ResultsPage':
        self.py.get(self.LOADER_SPINNER) \
            .should().have_attr('style', 'display: block;') \
            .should().have_attr('style', 'display: none;')
        return self
