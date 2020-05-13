from pprint import pprint


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
