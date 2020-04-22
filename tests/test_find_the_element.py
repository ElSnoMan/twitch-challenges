
def test_zoro_login(py):
    py.visit('https://zoro.co.uk')
    py.get(css="[id='HeaderMenu.showLoginDialogButton']").click()
    py.get("[data-e2e='emailAddress']").type('foo@email.com').should().have_value('foo@email.com')
    py.get("[data-e2e='password']").type('our-mom')
    pass


def test_find_articles_in_sections(py):
    py.visit('https://www.bostonglobe.com/metro/')
    assert py.xpath("//section[@id='sp-top-main']//a").length == 6
    assert py.find("[class*='feature_feed'] li a").length == 10
