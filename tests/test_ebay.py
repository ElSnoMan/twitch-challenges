import pytest


RADIO_BUTTON = "[data-value='US Only']"
CHECK_BOXES_COMPLETE_ITEMS = "[aria-label='Completed Items']"
PRICE_FROM = "//input[@class='x-textrange__input x-textrange__input--from']"
PRICE_TO = "//input[@class='x-textrange__input x-textrange__input--to']"


@pytest.fixture
def ebay_visit(py):
    py.visit("https://www.ebay.com/")
    py.get_xpath("//input[@id='gh-ac']").type("1/35 rye field model jagdpanther").submit()


def test_price_range(py, ebay_visit):
    py.get_xpath(PRICE_FROM).type("20").should().have_value('20')
    py.get_xpath(PRICE_TO).type("70").should().have_value('70').click()


def test_radio_buttons(py, ebay_visit):
    assert not py.get(RADIO_BUTTON).is_checked()
    py.get(RADIO_BUTTON).check().should().disappear()
    assert py.get(RADIO_BUTTON).should().be_checked()
