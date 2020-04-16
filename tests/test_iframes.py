
def test_switch_to_iframe_space_jam(py):
    py.visit("https://spacejam.com/cmp/lineup/lineupframes.html")
    py.switch_to.frame('main')
    py.contains('The cast')


def test_switch_to_iframe(py):
    py.visit('https://the-internet.herokuapp.com/iframe')
    py.switch_to.frame('mce_0_ifr')
    py.get('#tinymce').clear().type('Lunch Brunch Bunch')\
        .should().have_value('Lunch Brunch Bunch')
