from selene import be, have
from selene.support.shared import browser


def test_first():
    browser.element('[name="q"]').should(be.blank).type('selene github').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_second_negative():
    browser.element('[name="q"]').should(be.blank).type('selenide github').press_enter()
    browser.element('[id="search"]').should(have.no.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
