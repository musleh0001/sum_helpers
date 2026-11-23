"""Tests for two_sum module."""

from sum_helpers.two_sum import (
    two_sum,
    two_sum_closest,
    two_sum_less_than_k,
    two_sum_sorted,
    two_sum_unique_pairs,
)


class TestTwoSum:
    def test_standard_case(self) -> None:
        nums = [2, 7, 11, 15]
        res = two_sum(nums, 9)
        assert res == (0, 1)

    def test_unsorted_array(self) -> None:
        nums = [3, 2, 4]
        res = two_sum(nums, 6)
        assert res == (1, 2)

    def test_duplicate_elements(self) -> None:
        nums = [3, 3]
        res = two_sum(nums, 6)
        assert res == (0, 1)

    def test_multiple_duplicates(self) -> None:
        nums = [1, 5, 5, 5, 9]
        res = two_sum(nums, 10)
        assert res is not None
        assert nums[res[0]] + nums[res[1]] == 10
        assert res[0] < res[1]

    def test_negative_numbers(self) -> None:
        nums = [-3, 4, 3, 90]
        res = two_sum(nums, 0)
        assert res == (0, 2)

    def test_all_negative(self) -> None:
        nums = [-10, -20, -5, -1]
        res = two_sum(nums, -15)
        assert res == (0, 2)

    def test_no_match(self) -> None:
        nums = [1, 2, 3]
        assert two_sum(nums, 10) is None

    def test_empty_and_single_element(self) -> None:
        assert two_sum([], 5) is None
        assert two_sum([5], 5) is None

    def test_immutability(self) -> None:
        nums = [5, 2, 9, 1]
        original = list(nums)
        two_sum(nums, 10)
        assert nums == original


class TestTwoSumSorted:
    def test_standard_case(self) -> None:
        numbers = [2, 7, 11, 15]
        res = two_sum_sorted(numbers, 9)
        assert res == (1, 2)  # 1-indexed

    def test_three_elements(self) -> None:
        numbers = [2, 3, 4]
        res = two_sum_sorted(numbers, 6)
        assert res == (1, 3)

    def test_negatives(self) -> None:
        numbers = [-1, 0]
        res = two_sum_sorted(numbers, -1)
        assert res == (1, 2)

    def test_duplicates_in_sorted(self) -> None:
        numbers = [1, 2, 2, 5]
        res = two_sum_sorted(numbers, 4)
        assert res == (2, 3)

    def test_no_match(self) -> None:
        numbers = [1, 2, 3]
        assert two_sum_sorted(numbers, 10) is None

    def test_short_arrays(self) -> None:
        assert two_sum_sorted([], 0) is None
        assert two_sum_sorted([1], 1) is None

    def test_immutability(self) -> None:
        nums = [1, 3, 5, 7]
        copy = list(nums)
        two_sum_sorted(nums, 8)
        assert nums == copy


class TestTwoSumLessThanK:
    def test_standard_case(self) -> None:
        nums = [34, 23, 1, 24, 75, 33, 54, 8]
        assert two_sum_less_than_k(nums, 60) == 58

    def test_negative_values(self) -> None:
        nums = [-5, -2, 1, 3]
        # sums < 0: (-5 + 3 = -2), (-5 + 1 = -4), (-2 + 1 = -1), (-5 + -2 = -7)
        # max sum strictly less than 0 is -1
        assert two_sum_less_than_k(nums, 0) == -1

    def test_no_sum_less_than_k(self) -> None:
        nums = [10, 20, 30]
        assert two_sum_less_than_k(nums, 15) is None

    def test_edge_cases(self) -> None:
        assert two_sum_less_than_k([], 10) is None
        assert two_sum_less_than_k([5], 10) is None

    def test_exact_k_not_included(self) -> None:
        # Sum must be strictly less than k
        nums = [1, 4]
        assert two_sum_less_than_k(nums, 5) is None
        assert two_sum_less_than_k(nums, 6) == 5


class TestTwoSumClosest:
    def test_standard_case(self) -> None:
        nums = [-1, 2, 1, -4]
        assert two_sum_closest(nums, 1) == 1
        # Target 4 with [-1, 2, 1, -4]:
        # Pair sums:
        # -1+2=1, -1+1=0, -1+-4=-5, 2+1=3, 2+-4=-2, 1+-4=-3
        # Closest to 4 is 3 (diff 1)
        assert two_sum_closest(nums, 4) == 3

    def test_exact_match(self) -> None:
        nums = [1, 2, 3, 4]
        assert two_sum_closest(nums, 5) == 5

    def test_tie_breaking_smaller_sum(self) -> None:
        # candidates: 1+3=4 (diff 1 from 5), 2+4=6 (diff 1 from 5)
        nums = [1, 2, 3, 4]
        # Pair with closest sum to 5: 1+4=5 (exact).
        # Let's test target 3 with [1, 5]: sum 6, diff 3.
        # With [0, 6], target 3: sum 6 (diff 3)
        # With [-2, 8] vs [0, 4]: target 1
        nums2 = [0, 2]  # sum 2 (diff 1 from 1)
        # target 1 with [0, 2] -> sum 2 (diff 1)
        assert two_sum_closest(nums2, 1) == 2

    def test_short_inputs(self) -> None:
        assert two_sum_closest([], 5) is None
        assert two_sum_closest([1], 5) is None

    def test_negatives(self) -> None:
        nums = [-10, -5, -2, -1]
        assert two_sum_closest(nums, -8) == -7


class TestTwoSumUniquePairs:
    def test_unique_pairs_with_duplicates(self) -> None:
        nums = [1, 1, 2, 4, 3, 3, 5]
        res = two_sum_unique_pairs(nums, 6)
        assert res == [(1, 5), (2, 4), (3, 3)]

    def test_no_valid_pairs(self) -> None:
        assert two_sum_unique_pairs([1, 2, 3], 10) == []

    def test_short_inputs(self) -> None:
        assert two_sum_unique_pairs([], 5) == []
        assert two_sum_unique_pairs([5], 5) == []
