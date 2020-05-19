from how_many_smaller_numbers.main import how_many_smaller_numbers


def test_one():
    nums = [8, 1, 2, 2, 3]
    assert how_many_smaller_numbers(nums) == [4, 0, 1, 1, 3]


def test_two():
    nums = [6, 5, 4, 8]
    assert how_many_smaller_numbers(nums) == [2, 1, 0, 3]


def test_three():
    nums = [7, 7, 7, 7]
    assert how_many_smaller_numbers(nums) == [0, 0, 0, 0]
