
def test_shadow_dom(py):
    py.visit('https://the-internet.herokuapp.com/shadowdom')
    shadow = py.find('my-paragraph')[1].open_shadow_dom()
    assert shadow.xpath('//*[@name="my-text"]').should().contain_text('My default text')

    items = [li.text for li in py.find('li')]
    assert len(items) == 2
    assert 'In a list!' in items
