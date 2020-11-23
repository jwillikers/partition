import pytest
from partition import partition


def test_should_accept_empty_string_for_seq():
    assert partition('', lambda x: x % 2 == 1) == ([], [])


def test_should_accept_empty_list_for_seq():
    assert partition([], lambda x: x % 2 == 1) == ([], [])


def test_should_accept_string_for_seq():
    assert partition('123ABC', str.isdigit) == (['A', 'B', 'C'], ['1', '2', '3'])


def test_should_accept_dict_for_seq():
    assert partition({1: 'A', 2: 'B', 3: 'C'}, lambda x: x % 2 == 1) == ([2], [1, 3])


def test_should_partition_the_example_correctly():
    assert partition(range(10), lambda x: x % 2 == 1) == ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])


def test_should_reject_bool_for_pred():
    with pytest.raises(TypeError):
        partition(range(10), True)


def test_should_reject_int_for_pred():
    with pytest.raises(TypeError):
        partition(range(10), 0)


def test_should_reject_string_for_pred():
    with pytest.raises(TypeError):
        partition(range(10), 'test')
