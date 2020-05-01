from typing import List


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = ''
        self.family_members: List[User] = []


def login(user):
    print(user.email)
    print(user.password)
    # db.get_user(user.email)
    user.family_members = [
        User('test@example.com', 'pw'),
        User('test2@example.com', 'pw2')
    ]


def main():
    carlos = User('carlos@email.com', 'password')
    login(carlos)
    print(carlos.family_members)


if __name__ == '__main__':
    main()
