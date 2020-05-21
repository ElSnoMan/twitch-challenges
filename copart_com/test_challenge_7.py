"""
1. Go to copart.com
2. Look at the Makes/Models section of the page
3. Create a two-dimensional list that stores the names of the Make/Model as well as their URLs
4. Check that each element in this list navigates to the correct page
"""
from pprint import pprint

MAKES_AND_MODELS = "//a[contains(@href, 'popular/make') or contains(@href, 'popular/model')]"


def test_ch7(py):
    py.visit('https://copart.com')
    cars = []
    for make_model in py.find_xpath(MAKES_AND_MODELS):
        name = make_model.text()
        url = make_model.get_attribute('href')
        cars.append([name, url])
    # pprint(cars)
    for car in cars:
        name, url = car
        py.visit(url)
        assert py.contains(name.lower())
