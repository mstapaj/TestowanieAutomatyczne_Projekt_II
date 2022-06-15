import pytest

from tests.test_item import fakereturn


def test_fakereturn():
    assert fakereturn(1) == {'id': 1, 'name': 'Piłka', 'value': 35.99}


def test_fakereturn_zero():
    with pytest.raises(ValueError):
        fakereturn(0)


def test_fakereturn_two():
    with pytest.raises(ValueError):
        fakereturn(2)


def test_fakereturn_none():
    with pytest.raises(ValueError):
        fakereturn(None)


def test_fakereturn_object():
    with pytest.raises(ValueError):
        fakereturn([])


def test_fakereturn_array():
    with pytest.raises(ValueError):
        fakereturn({})


def test_fakereturn_true():
    with pytest.raises(ValueError):
        fakereturn(True)


def test_fakereturn_false():
    with pytest.raises(ValueError):
        fakereturn(False)


def test_fakereturn_string():
    with pytest.raises(ValueError):
        fakereturn('abcdef')


def test_fakereturn_empty_string():
    with pytest.raises(ValueError):
        fakereturn('')


def test_fakereturn_int():
    with pytest.raises(ValueError):
        fakereturn(12)


def test_fakereturn_float():
    with pytest.raises(ValueError):
        fakereturn(4.12)


def test_fakereturn_negative_int():
    with pytest.raises(ValueError):
        fakereturn(-3)


def test_fakereturn_negative_float():
    with pytest.raises(ValueError):
        fakereturn(-7.12)
