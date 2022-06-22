from selene import be, have
from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def open_google():
    browser.open('https://google.com/ncr')


@pytest.fixture(autouse=True)
def window_size(open_google):
    browser.driver.set_window_size(width=1920, height=1080)


def test_first():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second_negative():
    browser.element('[name="q"]').should(be.blank).type('dfewtggshefwewf').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
