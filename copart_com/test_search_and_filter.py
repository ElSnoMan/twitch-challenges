from selenium.webdriver.common.keys import Keys

from copart_com.pages.home import HomePage


def test_stg_ch6(py):
    py.visit('https://copart.com')
    py.get('#input-search').type('nissan', Keys.ENTER)
    py.get("input[type='search']").type('SKYLINE22')
    py.get('#serverSideDataTable_processing') \
        .should().have_attr('style', 'display: block;') \
        .should().have_attr('style', 'display: none;')
    assert py.contains('SKYLINE')


def test_stg_ch6_pom(py):
    results_page = HomePage(py).visit().search('nissan')
    results_page.filter_search('SKYLINE22')
    assert py.contains('SKYLINE')
