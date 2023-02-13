import pytest
from conftest import setup
# def test_example(setup):
#     print("this is a sample example")

# def test_sample(setup):
#     print("sample example 2")

@pytest.mark.usefixtures('setup')
class Test_login:

    def test_example(self):
        print("this is a sample example")

    def test_sample(self):
        print("sample example 2")
