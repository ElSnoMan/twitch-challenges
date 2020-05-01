from pylenium import Pylenium


class ResultsPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def title(self) -> str:
        return self.py.title
