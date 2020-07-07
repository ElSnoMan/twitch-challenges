
def get_word_in_string_with_length(string: str, length: int) -> str:
    for txt in string.split():
        if len(txt) > length:
            return txt
    return ''


def get_longest_word(string: str) -> str:
    words = string.split()
    return max(words, key=len)


def test_dynamic_content(py):
    py.visit('https://the-internet.herokuapp.com/dynamic_content')
    text = py.get("[id='content'] [class='row']").text()
    word = get_word_in_string_with_length(text, 10)
    assert word


def test_longest_word():
    string = "these are some longer words: pandemic, disease, etc"
    assert get_longest_word(string) == 'pandemic'
