from pprint import pprint

from selenium.webdriver.common.keys import Keys


def test_find_select_country(py):
    py.visit('https://www.hobbyeasy.com/en/category/AF35K/50/1/maker/all.html')
    # count names of makers
    assert py.find("[href*='makers']").should().have_length(50)
    # count how much every items in maker
    makers = dict()
    for maker in py.find("[href*='makers']"):  # Hasegawa
        if maker.text() in makers:
            makers[maker.text()] += 1
        else:
            makers[maker.text()] = 1

    pprint(makers)


def test_searchfield_7235(py):
    """in search field is present phrase "Select item".
    when you type for example article number of item we have as result 'Nothing matches to this item'
    That's why 'Select item'+'type. How to clean up this search field?"""
    py.visit('http://72-35.ru/')
    py.get('#seachTextField').click()
    py.get('#seachTextField').type('6600')
    py.get('#hnSearchButton').click()


def test_amazon_clear_stuff(py):
    py.visit('https://amazon.com')
    py.get('#twotabsearchtextbox').type('LOL', Keys.ENTER)
    py.wait(lambda _: py.execute_script('return document.readyState') == 'complete')
    assert py.get('#twotabsearchtextbox').clear()
    py.get('#twotabsearchtextbox').should().have_attr('value', '')
