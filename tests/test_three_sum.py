"""Tests for three_sum module."""

from sum_helpers.three_sum import (
    three_sum,
    three_sum_closest,
    three_sum_smaller,
)


class TestThreeSum:
    def test_standard_case(self) -> None:
        nums = [-1, 0, 1, 2, -1, -4]
        res = three_sum(nums, target=0)
        assert res == [(-1, -1, 2), (-1, 0, 1)]

    def test_no_solution(self) -> None:
        assert three_sum([0, 1, 1], target=0) == []

    def test_all_zeros(self) -> None:
        assert three_sum([0, 0, 0], target=0) == [(0, 0, 0)]
        assert three_sum([0, 0, 0, 0, 0], target=0) == [(0, 0, 0)]

    def test_custom_target(self) -> None:
        nums = [1, 2, 3, 4, 5]
        res = three_sum(nums, target=9)
        # 1+3+5=9, 2+3+4=9
        assert res == [(1, 3, 5), (2, 3, 4)]

    def test_negative_target(self) -> None:
        nums = [-5, -2, -1, 0, 2]
        res = three_sum(nums, target=-4)
        # -5 + -1 + 2 = -4
        # -5 + -2 + 3 (no 3)
        # -2 + -2 ...
        assert (-5, -1, 2) in res

    def test_short_inputs(self) -> None:
        assert three_sum([], 0) == []
        assert three_sum([1], 0) == []
        assert three_sum([1, 2], 0) == []

    def test_immutability(self) -> None:
        nums = [3, -1, 0, -2, 2, 1]
        copy = list(nums)
        three_sum(nums)
        assert nums == copy


class TestThreeSumClosest:
    def test_standard_case(self) -> None:
        nums = [-1, 2, 1, -4]
        assert three_sum_closest(nums, target=1) == 2

    def test_exact_match(self) -> None:
        nums = [0, 0, 0]
        assert three_sum_closest(nums, target=0) == 0

    def test_negative_target(self) -> None:
        nums = [-5, -4, -3, -2, -1]
        assert three_sum_closest(nums, target=-10) == -10

    def test_large_target(self) -> None:
        nums = [1, 1, 1, 1]
        assert three_sum_closest(nums, target=100) == 3

    def test_short_inputs(self) -> None:
        assert three_sum_closest([], 1) is None
        assert three_sum_closest([1], 1) is None
        assert three_sum_closest([1, 2], 1) is None

    def test_immutability(self) -> None:
        nums = [4, 1, -2, 7]
        copy = list(nums)
        three_sum_closest(nums, 5)
        assert nums == copy


class TestThreeSumSmaller:
    def test_standard_case(self) -> None:
        nums = [-2, 0, 1, 3]
        # Valid index triplets:
        # (-2, 0, 1) -> sum -1 < 2
        # (-2, 0, 3) -> sum 1 < 2
        assert three_sum_smaller(nums, target=2) == 2

    def test_empty_and_short_inputs(self) -> None:
        assert three_sum_smaller([], 0) == 0
        assert three_sum_smaller([0], 0) == 0
        assert three_sum_smaller([1, 2], 3) == 0

    def test_all_triplets_valid(self) -> None:
        nums = [1, 2, 3]
        assert three_sum_smaller(nums, target=10) == 1

    def test_no_triplets_valid(self) -> None:
        nums = [5, 6, 7]
        assert three_sum_smaller(nums, target=10) == 0

    def test_duplicates(self) -> None:
        # [1, 1, 1], sum=3 < 4 -> 1 triplet
        assert three_sum_smaller([1, 1, 1], target=4) == 1
        # [1, 1, 1, 1], choose 3 out of 4 = 4 triplets, all sum 3 < 4
        assert three_sum_smaller([1, 1, 1, 1], target=4) == 4

    def test_immutability(self) -> None:
        nums = [3, 1, 2]
        copy = list(nums)
        three_sum_smaller(nums, 10)
        assert nums == copy
