"""Three Sum helper functions.

This module provides solutions for classic Three Sum problem variants:
- LC 15: 3Sum (unique triplets summing to target, default 0)
- LC 16: 3Sum Closest (sum of three integers closest to target)
- LC 259: 3Sum Smaller (count of index triplets summing to strictly less than target)
"""

from __future__ import annotations

from typing import Sequence

__all__ = [
    "three_sum",
    "three_sum_closest",
    "three_sum_smaller",
]


def three_sum(nums: Sequence[int], target: int = 0) -> list[tuple[int, int, int]]:
    """Find all unique triplets [a, b, c] summing to target (LeetCode 15).

    Assumptions & Behavior:
    - Input can be unsorted and may contain duplicates or negative numbers.
    - Triplets are unique (no duplicates in the result set).
    - Each triplet (a, b, c) is sorted such that a <= b <= c.
    - If len(nums) < 3, returns an empty list [].
    - Pure function: does not mutate the caller's input.

    Args:
        nums: A sequence of integers.
        target: The target sum (defaults to 0 as in LC 15).

    Returns:
        A list of unique triplets (a, b, c) where a + b + c == target and a <= b <= c.

    Complexity:
        Time: O(n^2) where n is len(nums).
        Space: O(n) for the sorted copy.

    Examples:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [(-1, -1, 2), (-1, 0, 1)]
        >>> three_sum([0, 1, 1])
        []
        >>> three_sum([0, 0, 0])
        [(0, 0, 0)]
    """
    n = len(nums)
    if n < 3:
        return []

    sorted_nums = sorted(nums)
    triplets: list[tuple[int, int, int]] = []

    for i in range(n - 2):
        val_i = sorted_nums[i]

        # Skip duplicate values for the first element
        if i > 0 and val_i == sorted_nums[i - 1]:
            continue

        # Pruning optimizations based on sorted order:
        # Minimum possible sum with current element exceeds target -> stop
        if val_i + sorted_nums[i + 1] + sorted_nums[i + 2] > target:
            break
        # Maximum possible sum with current element is below target -> skip to next
        if val_i + sorted_nums[-2] + sorted_nums[-1] < target:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = val_i + sorted_nums[left] + sorted_nums[right]

            if curr_sum == target:
                triplets.append((val_i, sorted_nums[left], sorted_nums[right]))
                left += 1
                right -= 1

                # Skip duplicates for second and third elements
                while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return triplets


def three_sum_closest(nums: Sequence[int], target: int) -> int | None:
    """Find the sum of three integers closest to target (LeetCode 16).

    Assumptions & Behavior:
    - Input can be unsorted and contain duplicates or negative numbers.
    - If len(nums) < 3, returns None.
    - Tie-breaking: If two sums have equal distance to target, the smaller sum is returned.
    - Returns exact target immediately if a triplet sum equals target.
    - Pure function: does not mutate the caller's input.

    Args:
        nums: A sequence of integers.
        target: The target integer to approximate.

    Returns:
        The sum of three integers closest to target, or None if len(nums) < 3.

    Complexity:
        Time: O(n^2) where n is len(nums).
        Space: O(n) for the sorted copy.

    Examples:
        >>> three_sum_closest([-1, 2, 1, -4], 1)
        2
        >>> three_sum_closest([0, 0, 0], 1)
        0
        >>> three_sum_closest([1, 1], 2) is None
        True
    """
    n = len(nums)
    if n < 3:
        return None

    sorted_nums = sorted(nums)
    closest_sum = sorted_nums[0] + sorted_nums[1] + sorted_nums[2]

    for i in range(n - 2):
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue

        val_i = sorted_nums[i]
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = val_i + sorted_nums[left] + sorted_nums[right]

            if curr_sum == target:
                return target

            curr_diff = abs(curr_sum - target)
            best_diff = abs(closest_sum - target)

            if curr_diff < best_diff or (curr_diff == best_diff and curr_sum < closest_sum):
                closest_sum = curr_sum

            if curr_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


def three_sum_smaller(nums: Sequence[int], target: int) -> int:
    """Count index triplets (i, j, k) with i < j < k whose sum is strictly less than target (LeetCode 259).

    Assumptions & Behavior:
    - Input can be unsorted and may contain duplicates and negative numbers.
    - Counts index triplets: identical values at distinct indices are counted separately.
    - If len(nums) < 3, returns 0.
    - Pure function: does not mutate the caller's input.

    Args:
        nums: A sequence of integers.
        target: The target sum upper bound (strictly less than).

    Returns:
        The total number of index triplets (i, j, k) with i < j < k and nums[i] + nums[j] + nums[k] < target.

    Complexity:
        Time: O(n^2) where n is len(nums).
        Space: O(n) for the sorted copy.

    Examples:
        >>> three_sum_smaller([-2, 0, 1, 3], 2)
        2
        >>> three_sum_smaller([], 0)
        0
        >>> three_sum_smaller([0], 0)
        0
    """
    n = len(nums)
    if n < 3:
        return 0

    sorted_nums = sorted(nums)
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if curr_sum < target:
                # Since sorted_nums is non-decreasing, all elements between left and right
                # paired with sorted_nums[i] and sorted_nums[left] will also sum to < target.
                count += right - left
                left += 1
            else:
                right -= 1

    return count
