"""
Validate the complexity of a proposed password by assuring
it meets these rules:

* at least 8 characters
* contains an uppercase letter
* contains a special character
* does not contain the username
* is not the same as the old password
"""
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


def validate_password_length(password: str) -> str:
    if len(password) < 8:
        return 'Password must be greater than 8 characters'
    else:
        return ''


def validate_password_has_uppercase(password: str) -> str:
    for ch in password:
        if ch.isupper():
            return ''
    return 'Password must include one uppercase letter'


def validate_password_has_special_character(password: str) -> str:
    special_chars = '[@_!#$%^&*()<>?/\\|}{~:]-;'
    for ch in password:
        if ch in special_chars:
            return ''
    return 'Password must include one special character'


def validate_password_does_not_contain_username(password: str, username: str) -> str:
    if username.upper() in password.upper():
        return 'Password must not include your username'
    return ''


def validate_password_does_not_match_old_password(password: str, old_password: str) -> str:
    if password == old_password:
        return 'Password cannot be the same as your old password'
    return ''


def check_password():
    user = User(username='foo', password='bar')
    new_password = input('Enter a new password: ')

    errors = list()
    errors.append(validate_password_length(new_password))
    errors.append(validate_password_has_uppercase(new_password))
    errors.append(validate_password_has_special_character(new_password))
    errors.append(validate_password_does_not_contain_username(new_password, user.username))
    errors.append(validate_password_does_not_match_old_password(new_password, user.password))

    for err in errors:
        if err:
            print(err)


if __name__ == '__main__':
    check_password()
