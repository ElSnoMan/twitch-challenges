
def test_dropdown_and_suggestions(py):
    py.visit('https://amazon.com')
    py.get('#searchDropdownBox').select('Toys & Games')
    py.get('#twotabsearchtextbox').type('LOL')

    py.get("#suggestions > div").click()
    text = py.get('#twotabsearchtextbox').get_attribute('value')

    assert py.get('[cel_widget_id="RESULT_INFO_BAR-RESULT_INFO_BAR"]').contains(text)
