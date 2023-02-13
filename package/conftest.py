import pytest

@pytest.fixture(scope='class')
def setup():
    print("This will run first")
    yield
    print("this will run in end")

def pytest_html_report_title(report):
    report.title = "My very own title!"
