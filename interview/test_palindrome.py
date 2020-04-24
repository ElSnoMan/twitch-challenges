
# write a function that tells us if a string is a palindrome


def is_palindrome(string):
    """ Compare original string with its reverse."""
    # [::-1] reverses a string
    reverse = string[::-1]
    return string == reverse


def test_is_palindrome():
    assert is_palindrome('banana') is False
    assert is_palindrome('foof')
