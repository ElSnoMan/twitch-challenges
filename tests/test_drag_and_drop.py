
def test_drag_to_with_selector(py):
    py.visit('https://the-internet.herokuapp.com/drag_and_drop')
    py.get('#column-a').drag_to('#column-b')
    assert py.get('#column-b > header').should().have_text('A')
