import pytest


@pytest.fixture
def browser():
    print("Я выполняюсь перед тестом. Открываем браузер!")

    yield "Browser"

    print("Я выполняюсь после теста. Браузер закрыт! Чистим кеш!")


@pytest.fixture
def login_page(browser):
    pass


@pytest.fixture
def credentials():
    return "admin", "12345"


def test_login(login_page, credentials):
    assert credentials == ("admin", "12345"), "Некорректный логин и пароль"
