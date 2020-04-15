
def test_basic_auth(py):
    # https://<username>:<password>@the-internet.herokuapp.com/basic_auth
    py.visit('https://admin:admin@the-internet.herokuapp.com')
    py.contains('Basic Auth').click()
    py.contains('Congratulations!')
