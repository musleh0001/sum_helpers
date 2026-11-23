"""Two Sum helper functions.

This module provides solutions for classic Two Sum variants:
- LC 1: Two Sum (hash table approach on unsorted sequence)
- LC 167: Two Sum II - Input Array Is Sorted (two-pointer approach on sorted sequence)
- LC 1099: Two Sum Less Than K (maximum sum strictly less than k)
- Two Sum Closest (sum of two numbers closest to target)
- Two Sum Unique Pairs (all unique value pairs summing to target)
"""

from __future__ import annotations

from typing import Sequence

__all__ = [
    "two_sum",
    "two_sum_sorted",
    "two_sum_less_than_k",
    "two_sum_closest",
    "two_sum_unique_pairs",
]


def two_sum(nums: Sequence[int], target: int) -> tuple[int, int] | None:
    """Find 0-indexed indices of two numbers that add up to target (LeetCode 1).

    Assumptions & Behavior:
    - Input can be unsorted.
    - Returns indices (i, j) with i < j of the first matching pair encountered.
    - If no two numbers add up to target, or if len(nums) < 2, returns None.
    - Does not mutate the input sequence.

    Args:
        nums: A sequence of integers.
        target: The target sum.

    Returns:
        A tuple (i, j) of 0-based indices such that nums[i] + nums[j] == target,
        or None if no valid pair exists.

    Complexity:
        Time: O(n) where n is len(nums), single pass with hash table lookup.
        Space: O(n) for the hash table in the worst case.

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
        >>> two_sum([3, 2, 4], 6)
        (1, 2)
        >>> two_sum([3, 3], 6)
        (0, 1)
        >>> two_sum([1, 2], 5) is None
        True
    """
    if len(nums) < 2:
        return None

    # Map value to its earliest observed index
    seen: dict[int, int] = {}
    for j, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], j
        if num not in seen:
            seen[num] = j

    return None


def two_sum_sorted(numbers: Sequence[int], target: int) -> tuple[int, int] | None:
    """Find 1-indexed indices of two numbers in a sorted array summing to target (LeetCode 167).

    Assumptions & Behavior:
    - Input numbers MUST be sorted in non-decreasing order.
    - Returns 1-indexed indices (i, j) with 1 <= i < j <= len(numbers).
    - If no pair sums to target, or len(numbers) < 2, returns None.
    - Uses the optimal two-pointer technique without extra memory.
    - Does not mutate the input sequence.

    Args:
        numbers: A sorted sequence of integers in non-decreasing order.
        target: The target sum.

    Returns:
        A 1-indexed tuple (i, j) such that numbers[i - 1] + numbers[j - 1] == target,
        or None if no valid pair exists.

    Complexity:
        Time: O(n) where n is len(numbers).
        Space: O(1) auxiliary space.

    Examples:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        (1, 2)
        >>> two_sum_sorted([2, 3, 4], 6)
        (1, 3)
        >>> two_sum_sorted([-1, 0], -1)
        (1, 2)
        >>> two_sum_sorted([1, 2], 10) is None
        True
    """
    if len(numbers) < 2:
        return None

    left = 0
    right = len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return left + 1, right + 1
        if curr_sum < target:
            left += 1
        else:
            right -= 1

    return None


def two_sum_less_than_k(nums: Sequence[int], k: int) -> int | None:
    """Find the maximum sum of two distinct elements strictly less than k (LeetCode 1099).

    Assumptions & Behavior:
    - Input can be unsorted.
    - Finds max(nums[i] + nums[j]) such that i < j and nums[i] + nums[j] < k.
    - If no pair has sum < k, or if len(nums) < 2, returns None.
    - Pure function: does not mutate the caller's list (sorts a copy).

    Args:
        nums: A sequence of integers.
        k: The upper threshold (strictly greater than the desired sum).

    Returns:
        The maximum sum strictly less than k, or None if no such sum exists.

    Complexity:
        Time: O(n log n) due to sorting, where n is len(nums).
        Space: O(n) for the sorted copy.

    Examples:
        >>> two_sum_less_than_k([34, 23, 1, 24, 75, 33, 54, 8], 60)
        58
        >>> two_sum_less_than_k([10, 20, 30], 15) is None
        True
    """
    if len(nums) < 2:
        return None

    sorted_nums = sorted(nums)
    left = 0
    right = len(sorted_nums) - 1
    max_sum: int | None = None

    while left < right:
        curr_sum = sorted_nums[left] + sorted_nums[right]
        if curr_sum < k:
            if max_sum is None or curr_sum > max_sum:
                max_sum = curr_sum
            left += 1
        else:
            right -= 1

    return max_sum


def two_sum_closest(nums: Sequence[int], target: int) -> int | None:
    """Find the sum of two integers closest to the target.

    Assumptions & Behavior:
    - Input can be unsorted.
    - If len(nums) < 2, returns None.
    - Tie-breaking: If two candidate sums are equally distant from target
      (e.g., target 10, candidates 8 and 12), the smaller sum is returned.
    - Pure function: sorts a shallow copy without modifying the original input.

    Args:
        nums: A sequence of integers.
        target: The target sum to approximate.

    Returns:
        The sum of two elements whose sum is closest to target, or None if len(nums) < 2.

    Complexity:
        Time: O(n log n) where n is len(nums), dominated by sorting.
        Space: O(n) for the sorted copy.

    Examples:
        >>> two_sum_closest([-1, 2, 1, -4], 1)
        1
        >>> two_sum_closest([1, 10, 20], 8)
        11
    """
    if len(nums) < 2:
        return None

    sorted_nums = sorted(nums)
    left = 0
    right = len(sorted_nums) - 1
    closest_sum = sorted_nums[left] + sorted_nums[right]

    while left < right:
        curr_sum = sorted_nums[left] + sorted_nums[right]
        curr_diff = abs(curr_sum - target)
        best_diff = abs(closest_sum - target)

        if curr_diff < best_diff or (curr_diff == best_diff and curr_sum < closest_sum):
            closest_sum = curr_sum

        if curr_sum == target:
            return target
        if curr_sum < target:
            left += 1
        else:
            right -= 1

    return closest_sum


def two_sum_unique_pairs(nums: Sequence[int], target: int) -> list[tuple[int, int]]:
    """Find all unique pairs of values (a, b) with a <= b that sum to target.

    Assumptions & Behavior:
    - Input can be unsorted and may contain duplicates.
    - Returns unique pairs of values (not indices), ordered such that a <= b.
    - The returned list of pairs is sorted in ascending order of the first element.
    - Pure function: creates a sorted copy.

    Args:
        nums: A sequence of integers.
        target: The target sum.

    Returns:
        A list of unique tuples (a, b) such that a + b == target and a <= b.

    Complexity:
        Time: O(n log n) due to sorting.
        Space: O(n) for sorted copy and output list.

    Examples:
        >>> two_sum_unique_pairs([1, 1, 2, 4, 3, 3, 5], 6)
        [(1, 5), (2, 4), (3, 3)]
        >>> two_sum_unique_pairs([1, 2, 3], 10)
        []
    """
    if len(nums) < 2:
        return []

    sorted_nums = sorted(nums)
    left = 0
    right = len(sorted_nums) - 1
    pairs: list[tuple[int, int]] = []

    while left < right:
        curr_sum = sorted_nums[left] + sorted_nums[right]
        if curr_sum == target:
            pairs.append((sorted_nums[left], sorted_nums[right]))
            left += 1
            right -= 1
            while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                left += 1
            while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                right -= 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return pairs
