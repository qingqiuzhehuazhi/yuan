import pytest


@pytest.fixture(scope='function')
def operation_fixture():
    print("\n------------------前置条件----------------")
    yield
    print("\n------------------预期结果----------------")
