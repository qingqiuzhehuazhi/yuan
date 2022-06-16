import pytest
import requests


@pytest.fixture(scope='function')
def all_fixture():
    print("\n前置")
    yield
    print("\n后置")



