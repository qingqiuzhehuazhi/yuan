import pytest


@pytest.fixture(scope='function')
def merchant_fixture():
    print("\n前置")
    yield
    print("\n后置")
