import pytest


@pytest.fixture(autouse=True)
def main_digit_of_the_universe():
    pytest.num = 42

    yield

    pytest.num = 0
    assert pytest.num == 0


def test_main_digit_of_the_universe():
    assert pytest.num == 42
