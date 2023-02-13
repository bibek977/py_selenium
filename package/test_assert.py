import pytest

@pytest.mark.runthis
def test_assert_2():
    assert 10 == 10, 'Hello bhattarai'
  
# @pytest.mark.skip
@pytest.mark.xfail
def test_assert():
    assert 2 == 3, "Hello bibek"

# simple run == pytest -s
# single run == pytest test_assert -s
# same keyword run == pytest -k asse -s
# selective run == pytest -m runthis -s 
# selective run == pytest -m runthis -s -v for more details
# selective run == pytest -s -v test_print.py::test_print for more details