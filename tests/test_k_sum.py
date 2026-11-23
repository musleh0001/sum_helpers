"""Tests for k_sum module."""

from sum_helpers.k_sum import (
    four_sum,
    four_sum_closest,
    four_sum_ii,
    four_sum_smaller,
    k_sum,
    k_sum_closest,
    k_sum_smaller,
)
from sum_helpers.three_sum import (
    three_sum,
    three_sum_closest,
    three_sum_smaller,
)


class TestKSum:
    def test_k_equals_2(self) -> None:
        nums = [1, 1, 2, 4, 3, 3, 5]
        res = k_sum(nums, target=6, k=2)
        assert res == [(1, 5), (2, 4), (3, 3)]

    def test_k_equals_3(self) -> None:
        nums = [-1, 0, 1, 2, -1, -4]
        res = k_sum(nums, target=0, k=3)
        assert res == [(-1, -1, 2), (-1, 0, 1)]
        # Must match three_sum exactly
        assert res == three_sum(nums, 0)

    def test_k_equals_4(self) -> None:
        nums = [1, 0, -1, 0, -2, 2]
        res = k_sum(nums, target=0, k=4)
        assert res == [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]

    def test_k_equals_5(self) -> None:
        nums = [1, 2, 3, 4, 5, 6, 7]
        # 1+2+3+4+5 = 15
        res = k_sum(nums, target=15, k=5)
        assert (1, 2, 3, 4, 5) in res

    def test_invalid_k_and_short_inputs(self) -> None:
        assert k_sum([1, 2, 3], target=6, k=1) == []
        assert k_sum([1, 2, 3], target=6, k=0) == []
        assert k_sum([1, 2], target=3, k=4) == []
        assert k_sum([], target=0, k=2) == []

    def test_pruning_out_of_bounds(self) -> None:
        # Sum is impossible because k * max < target
        assert k_sum([1, 2, 3], target=100, k=3) == []
        # Sum is impossible because k * min > target
        assert k_sum([10, 20, 30], target=5, k=3) == []

    def test_immutability(self) -> None:
        nums = [4, 1, -1, 2, 0]
        copy = list(nums)
        k_sum(nums, 0, 3)
        assert nums == copy


class TestKSumClosest:
    def test_k_equals_1(self) -> None:
        assert k_sum_closest([1, 5, 10], target=6, k=1) == 5
        assert k_sum_closest([10, 20], target=15, k=1) == 10  # tie-breaking smaller

    def test_k_equals_3_matches_three_sum_closest(self) -> None:
        nums = [-1, 2, 1, -4]
        res = k_sum_closest(nums, target=1, k=3)
        assert res == 2
        assert res == three_sum_closest(nums, 1)

    def test_k_equals_4(self) -> None:
        nums = [1, 0, -1, 0, -2, 2]
        assert k_sum_closest(nums, target=0, k=4) == 0

    def test_edge_cases(self) -> None:
        assert k_sum_closest([], target=5, k=2) is None
        assert k_sum_closest([1, 2], target=5, k=3) is None
        assert k_sum_closest([1, 2, 3], target=5, k=0) is None


class TestKSumSmaller:
    def test_k_equals_1(self) -> None:
        assert k_sum_smaller([1, 2, 3, 4], target=3, k=1) == 2

    def test_k_equals_3_matches_three_sum_smaller(self) -> None:
        nums = [-2, 0, 1, 3]
        res = k_sum_smaller(nums, target=2, k=3)
        assert res == 2
        assert res == three_sum_smaller(nums, 2)

    def test_k_equals_4(self) -> None:
        nums = [1, 1, 1, 1, 1]  # 5 elements, combinations of 4 = 5
        # all sum to 4
        assert k_sum_smaller(nums, target=5, k=4) == 5
        assert k_sum_smaller(nums, target=4, k=4) == 0

    def test_short_inputs(self) -> None:
        assert k_sum_smaller([], target=5, k=2) == 0
        assert k_sum_smaller([1, 2], target=5, k=3) == 0


class TestFourSum:
    def test_standard_case(self) -> None:
        nums = [1, 0, -1, 0, -2, 2]
        res = four_sum(nums, target=0)
        assert res == [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]

    def test_duplicates_only(self) -> None:
        nums = [2, 2, 2, 2, 2]
        assert four_sum(nums, target=8) == [(2, 2, 2, 2)]

    def test_no_solution(self) -> None:
        assert four_sum([1, 2, 3, 4], target=100) == []

    def test_short_inputs(self) -> None:
        assert four_sum([], 0) == []
        assert four_sum([1, 2, 3], 6) == []

    def test_large_numbers(self) -> None:
        nums = [1000000000, 1000000000, 1000000000, 1000000000]
        assert four_sum(nums, target=4000000000) == [
            (1000000000, 1000000000, 1000000000, 1000000000)
        ]


class TestFourSumVariants:
    def test_four_sum_closest(self) -> None:
        nums = [1, 0, -1, 0, -2, 2]
        assert four_sum_closest(nums, target=0) == 0
        assert four_sum_closest([0, 0, 0, 0], target=10) == 0
        assert four_sum_closest([1, 2, 3], target=5) is None

    def test_four_sum_smaller(self) -> None:
        nums = [1, 1, 1, 1]
        assert four_sum_smaller(nums, target=5) == 1
        assert four_sum_smaller(nums, target=4) == 0
        assert four_sum_smaller([1, 2, 3], target=10) == 0


class TestFourSumII:
    def test_standard_case(self) -> None:
        nums1 = [1, 2]
        nums2 = [-2, -1]
        nums3 = [-1, 2]
        nums4 = [0, 2]
        assert four_sum_ii(nums1, nums2, nums3, nums4) == 2

    def test_all_zeros(self) -> None:
        assert four_sum_ii([0], [0], [0], [0]) == 1

    def test_no_matches(self) -> None:
        assert four_sum_ii([1], [1], [1], [1]) == 0

    def test_empty_lists(self) -> None:
        assert four_sum_ii([], [1], [2], [3]) == 0
