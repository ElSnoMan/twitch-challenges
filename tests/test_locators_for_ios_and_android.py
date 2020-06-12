import pytest
from pylenium import Pylenium
import inspect


class Config:
    def __init__(self, platform):
        self.platform = platform


class PageBase:
    def __init__(self, py: Pylenium, config: Config):
        self.py = py
        self.config = config


class PageBase3:
    def __init__(self, py: Pylenium, config: Config):
        self.py = py
        self.config = config
        self.platform = config.platform.upper()
        self.locators = self.get_locators()

    def get_locators(self):
        members = inspect.getmembers(self)
        locators = dict()
        for member in members:
            if self.config.platform.upper() in member[0]:
                locators[member[0]] = member[1]
        return locators


class LoginPage1(PageBase):
    def __init__(self, py, config):
        super().__init__(py, config)

    ANDROID_USERNAME_FIELD = '#android-username'
    ANDROID_PASSWORD_FIELD = '#android_password'
    ANDROID_LOGIN_BUTTON = '#android-login'

    IOS_USERNAME_FIELD = '#ios-username'
    IOS_PASSWORD_FIELD = '#ios_password'
    IOS_LOGIN_BUTTON = '#ios-login'

    def login_with(self, username, password) -> 'LoginPage1':
        """
        Pros:
            * Control the steps within the flow per platform
        Cons:
            * Can get verbose and not too DRY
        """
        if self.config.platform == 'android':
            self.py.get(self.ANDROID_USERNAME_FIELD).type(username)
            self.py.get(self.ANDROID_PASSWORD_FIELD).type(password)
            self.py.get(self.ANDROID_LOGIN_BUTTON).click()
        elif self.config.platform == 'ios':
            self.py.get(self.IOS_USERNAME_FIELD).type(username)
            self.py.get(self.IOS_PASSWORD_FIELD).type(password)
            self.py.get(self.IOS_LOGIN_BUTTON).click()
        return self


class LoginPage2(PageBase):
    def __init__(self, py, config):
        super().__init__(py, config)

    android = {
        'username_field': 'android-username',
        'password_field': 'android-password',
        'login_button': 'android-login'
    }
    ios = {
        'username_field': 'ios-username',
        'password_field': 'ios-password',
        'login_button': 'ios-login'
    }

    def login_with(self, username, password) -> 'LoginPage2':
        """
        Pros:
            * Concise, more DRY
            * Dynamically change the locators dictionary given the platform
        Cons:
            * Most of the keys must be the same between android and ios dictionaries,
            but that's not too big of a deal.
        """
        locators = self.__getattribute__(self.config.platform.lower())
        self.py.get(locators['username_field']).type(username)
        self.py.get(locators['password_field']).type(password)
        self.py.get(locators['login_button']).click()
        return self


class LoginPage3(PageBase3):
    def __init__(self, py, config):
        super().__init__(py, config)

    ANDROID_USERNAME_FIELD = '#android-username'
    ANDROID_PASSWORD_FIELD = '#android_password'
    ANDROID_LOGIN_BUTTON = '#android-login'

    IOS_USERNAME_FIELD = '#ios-username'
    IOS_PASSWORD_FIELD = '#ios_password'
    IOS_LOGIN_BUTTON = '#ios-login'

    def login_with(self, username, password) -> 'LoginPage3':
        """
        Pros:
            * Concise, more DRY
            * Dynamically change the locators dictionary given the platform
            * No locator dictionary in the class, so UPPER_CASE constants
            * Flexibility of Option 1, ease of use of Option 2
        Cons:
            * Most of the keys must be the same between android and ios dictionaries,
            but that's not too big of a deal.
            * More complicated to setup
        """
        self.py.get(self.locators[f'{self.platform}_USERNAME_FIELD']).type(username)
        self.py.get(self.locators[f'{self.platform}_PASSWORD_FIELD']).type(password)
        self.py.get(self.locators[f'{self.platform}_LOGIN_BUTTON']).click()
        return self


@pytest.fixture
def config():
    def _config(platform):
        return Config(platform)
    return _config


def test_android_page_1(py, config):
    page = LoginPage1(py, config('android'))
    page.login_with('username', 'password')


def test_ios_page_1(py, config):
    page = LoginPage1(py, config('ios'))
    page.login_with('username', 'password')


def test_android_page_2(py, config):
    page = LoginPage2(py, config('android'))
    page.login_with('username', 'password')


def test_ios_page_2(py, config):
    page = LoginPage2(py, config('ios'))
    page.login_with('username', 'password')


def test_android_page_3(py, config):
    page = LoginPage3(py, config('android'))
    page.login_with('username', 'password')


def test_ios_page_3(py, config):
    page = LoginPage3(py, config('ios'))
    page.login_with('username', 'password')