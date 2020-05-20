def add(a: int, b: int) -> int:
    return a + b


def test_add_positive():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == 3


def test_add_str_numbers():
    assert add('1', '2') == 3


def test_add_strings():
    assert add('foo', 'bar') == 'foobar'


def test_add_lists():
    assert add(['foo'], ['bar']) == ['foo', 'bar']


# CRUD
class User:
    ID: str
    email: str
    name: str

# C
# create with valid inputs
# create with invalid inputs
# create with missing inputs
# create a duplicate User
# check responses

# R
# get User with valid inputs
# get User with invalid inputs
# search by just ID?
# search multiple users?
# get a non-existent User

# U
#

# D
# delete User with valid inputs
# delete User with invalid inputs
# what's required to delete a User?
# delete a non-existent
# soft-delete vs hard-delete?
