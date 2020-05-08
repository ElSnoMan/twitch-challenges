
def test_radio_buttons(py):
    py.visit('https://www.ebay.com/b/Video-Game-Consoles/139971/bn_320033')
    py.get("[aria-label='1 Day Shipping']").scroll_into_view().click(force=True)
    assert py.get("[aria-label='1 Day Shipping']").should().be_selected()
