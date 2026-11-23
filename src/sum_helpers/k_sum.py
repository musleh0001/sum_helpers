"""Generalized K-Sum and Four Sum helper functions.

This module provides generalized implementations for:
- 4Sum: All unique quadruplets summing to target
- 4Sum Closest: Quadruplet sum closest to target
- 4Sum Smaller: Count of index quadruplets summing to strictly less than target
- 4Sum II: Count index quadruplets across four separate arrays summing to zero
- Generalized K-Sum: Arbitrary k >= 2 unique tuple sum algorithm
- Generalized K-Sum Closest: Sum of k integers closest to target
- Generalized K-Sum Smaller: Count of index k-tuples summing to strictly less than target
"""

from __future__ import annotations

from collections import Counter
from typing import Sequence

__all__ = [
    "k_sum",
    "k_sum_closest",
    "k_sum_smaller",
    "four_sum",
    "four_sum_closest",
    "four_sum_smaller",
    "four_sum_ii",
]


def k_sum(nums: Sequence[int], target: int, k: int) -> list[tuple[int, ...]]:
    """Find all unique k-tuples in nums that sum to target.

    Assumptions & Behavior:
    - Input can be unsorted and may contain duplicate values and negative numbers.
    - Result contains unique sorted k-tuples: each tuple has elements in ascending
      order (x_1 <= x_2 <= ... <= x_k).
    - If k < 2 or len(nums) < k, returns an empty list [].
    - Employs pruning optimizations:
      1. If k * minimum remaining element > target, no combination can reach target.
      2. If k * maximum remaining element < target, no combination can reach target.
    - Base case k == 2 uses the optimal two-pointer two-sum approach.
    - Pure function: does not mutate the caller's input sequence.

    Args:
        nums: A sequence of integers.
        target: The desired target sum.
        k: The number of elements in each tuple (k >= 2).

    Returns:
        A list of unique k-tuples summing to target.

    Complexity:
        Time: O(n^(k-1)) where n is len(nums). For k=4, O(n^3); for k=3, O(n^2).
        Space: O(n + k) for sorted copy and recursion call stack.

    Examples:
        >>> k_sum([1, 0, -1, 0, -2, 2], target=0, k=4)
        [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]
        >>> k_sum([-1, 0, 1, 2, -1, -4], target=0, k=3)
        [(-1, -1, 2), (-1, 0, 1)]
        >>> k_sum([1, 2, 3], target=6, k=3)
        [(1, 2, 3)]
        >>> k_sum([1, 2], target=3, k=4)
        []
    """
    n = len(nums)
    if k < 2 or n < k:
        return []

    sorted_nums = sorted(nums)

    def _helper(start: int, sub_target: int, sub_k: int) -> list[list[int]]:
        res: list[list[int]] = []
        count = n - start
        if count < sub_k:
            return res

        min_val = sorted_nums[start]
        max_val = sorted_nums[-1]

        # Pruning: sub_target cannot be achieved by any elements in remaining range
        if sub_k * min_val > sub_target or sub_k * max_val < sub_target:
            return res

        # Base case: 2-Sum via two pointers
        if sub_k == 2:
            left = start
            right = n - 1
            while left < right:
                curr_sum = sorted_nums[left] + sorted_nums[right]
                if curr_sum == sub_target:
                    res.append([sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
                elif curr_sum < sub_target:
                    left += 1
                else:
                    right -= 1
            return res

        # Recursive case: sub_k > 2
        for i in range(start, n - sub_k + 1):
            val = sorted_nums[i]
            # Avoid duplicate elements at the current position
            if i > start and val == sorted_nums[i - 1]:
                continue

            # Additional early stopping bounds for the current loop element
            if val + (sub_k - 1) * sorted_nums[i + 1] > sub_target:
                break
            if val + (sub_k - 1) * max_val < sub_target:
                continue

            sub_results = _helper(i + 1, sub_target - val, sub_k - 1)
            for sub in sub_results:
                res.append([val] + sub)

        return res

    results = _helper(0, target, k)
    return [tuple(r) for r in results]


def k_sum_closest(nums: Sequence[int], target: int, k: int) -> int | None:
    """Find the sum of k elements in nums closest to target.

    Assumptions & Behavior:
    - Input can be unsorted and contain negative numbers or duplicates.
    - If k < 1 or len(nums) < k, returns None.
    - Tie-breaking: If two sums are equally distant from target, the smaller sum is returned.
    - Pure function: does not mutate caller's input.

    Args:
        nums: A sequence of integers.
        target: Target sum to approximate.
        k: Number of elements in each candidate combination (k >= 1).

    Returns:
        The sum of k elements closest to target, or None if len(nums) < k.

    Complexity:
        Time: O(n^(k-1)) where n is len(nums).
        Space: O(n + k) for sorted copy and recursion stack.

    Examples:
        >>> k_sum_closest([-1, 2, 1, -4], target=1, k=3)
        2
        >>> k_sum_closest([1, 1, 1, 0], target=100, k=4)
        3
    """
    n = len(nums)
    if k < 1 or n < k:
        return None

    sorted_nums = sorted(nums)

    if k == 1:
        best = sorted_nums[0]
        for val in sorted_nums:
            diff_curr = abs(val - target)
            diff_best = abs(best - target)
            if diff_curr < diff_best or (diff_curr == diff_best and val < best):
                best = val
        return best

    def _helper(start: int, sub_target: int, sub_k: int) -> int:
        if sub_k == 2:
            left = start
            right = n - 1
            closest = sorted_nums[left] + sorted_nums[right]
            while left < right:
                curr_sum = sorted_nums[left] + sorted_nums[right]
                if curr_sum == sub_target:
                    return sub_target

                diff_curr = abs(curr_sum - sub_target)
                diff_closest = abs(closest - sub_target)
                if diff_curr < diff_closest or (
                    diff_curr == diff_closest and curr_sum < closest
                ):
                    closest = curr_sum

                if curr_sum < sub_target:
                    left += 1
                else:
                    right -= 1
            return closest

        # sub_k > 2
        closest = sum(sorted_nums[start : start + sub_k])
        for i in range(start, n - sub_k + 1):
            if i > start and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            val = sorted_nums[i]
            # Prune if lowest possible sum from index i exceeds target and is worse than current best
            min_possible = val + sum(sorted_nums[i + 1 : i + sub_k])
            if min_possible > sub_target and abs(min_possible - sub_target) > abs(
                closest - sub_target
            ):
                break

            sub_closest = _helper(i + 1, sub_target - val, sub_k - 1)
            curr = val + sub_closest

            if curr == sub_target:
                return sub_target

            diff_curr = abs(curr - sub_target)
            diff_closest = abs(closest - sub_target)
            if diff_curr < diff_closest or (
                diff_curr == diff_closest and curr < closest
            ):
                closest = curr

        return closest

    return _helper(0, target, k)


def k_sum_smaller(nums: Sequence[int], target: int, k: int) -> int:
    """Count index k-tuples (i_1 < i_2 < ... < i_k) whose sum is strictly less than target.

    Assumptions & Behavior:
    - Input can be unsorted and may contain duplicates.
    - Counts combinations of indices: identical values at different positions are distinct.
    - If k < 1 or len(nums) < k, returns 0.
    - Pure function: does not mutate the caller's input.

    Args:
        nums: A sequence of integers.
        target: Target sum upper bound (strictly less than).
        k: Number of elements in each tuple.

    Returns:
        Total count of index k-tuples summing to < target.

    Complexity:
        Time: O(n^(k-1)) where n is len(nums).
        Space: O(n + k).

    Examples:
        >>> k_sum_smaller([-2, 0, 1, 3], target=2, k=3)
        2
        >>> k_sum_smaller([1, 1, 1, 1], target=5, k=4)
        1
    """
    n = len(nums)
    if k < 1 or n < k:
        return 0

    sorted_nums = sorted(nums)

    if k == 1:
        # Count elements < target
        return sum(1 for x in sorted_nums if x < target)

    def _helper(start: int, sub_target: int, sub_k: int) -> int:
        if sub_k == 2:
            left = start
            right = n - 1
            count = 0
            while left < right:
                if sorted_nums[left] + sorted_nums[right] < sub_target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count

        count = 0
        for i in range(start, n - sub_k + 1):
            # Prune if the minimum sum achievable from index i is >= sub_target
            if sum(sorted_nums[i : i + sub_k]) >= sub_target:
                break
            count += _helper(i + 1, sub_target - sorted_nums[i], sub_k - 1)

        return count

    return _helper(0, target, k)


def four_sum(nums: Sequence[int], target: int = 0) -> list[tuple[int, int, int, int]]:
    """Find all unique quadruplets [a, b, c, d] summing to target (LeetCode 18).

    Assumptions & Behavior:
    - Input can be unsorted and may contain duplicates and negative numbers.
    - Quadruplets are unique (deduplicated).
    - Each quadruplet is ordered: a <= b <= c <= d.
    - Returns [] if len(nums) < 4.
    - Pure function: does not mutate caller's input.

    Args:
        nums: A sequence of integers.
        target: The target sum (defaults to 0).

    Returns:
        A list of unique 4-tuples summing to target.

    Complexity:
        Time: O(n^3) where n is len(nums).
        Space: O(n) for the sorted copy.

    Examples:
        >>> four_sum([1, 0, -1, 0, -2, 2], 0)
        [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]
        >>> four_sum([2, 2, 2, 2, 2], 8)
        [(2, 2, 2, 2)]
    """
    results = k_sum(nums, target=target, k=4)
    return [t for t in results if len(t) == 4]  # type: ignore[misc]


def four_sum_closest(nums: Sequence[int], target: int) -> int | None:
    """Find the sum of four integers closest to target.

    Assumptions & Behavior:
    - If len(nums) < 4, returns None.
    - Tie-breaking: smaller sum preferred.
    - Pure function: does not mutate caller's input.

    Args:
        nums: A sequence of integers.
        target: Target sum.

    Returns:
        The sum of four elements closest to target, or None if len(nums) < 4.

    Complexity:
        Time: O(n^3) where n is len(nums).
        Space: O(n).

    Examples:
        >>> four_sum_closest([1, 0, -1, 0, -2, 2], 0)
        0
        >>> four_sum_closest([1, 1, 1], 5) is None
        True
    """
    return k_sum_closest(nums, target=target, k=4)


def four_sum_smaller(nums: Sequence[int], target: int) -> int:
    """Count index quadruplets (i, j, k, l) with i < j < k < l whose sum is strictly less than target.

    Assumptions & Behavior:
    - If len(nums) < 4, returns 0.
    - Counts index combinations.
    - Pure function: does not mutate caller's input.

    Args:
        nums: A sequence of integers.
        target: Strict upper bound sum.

    Returns:
        Count of index quadruplets with sum < target.

    Complexity:
        Time: O(n^3) where n is len(nums).
        Space: O(n).

    Examples:
        >>> four_sum_smaller([1, 1, 1, 1], 5)
        1
        >>> four_sum_smaller([1, 1, 1, 1], 4)
        0
    """
    return k_sum_smaller(nums, target=target, k=4)


def four_sum_ii(
    nums1: Sequence[int],
    nums2: Sequence[int],
    nums3: Sequence[int],
    nums4: Sequence[int],
) -> int:
    """Count quadruplets (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 (LeetCode 454).

    Assumptions & Behavior:
    - All four arrays can have different or identical lengths.
    - Works with negative numbers, duplicates, and zeros.
    - Uses a hash map to reduce O(n^4) brute force down to O(n^2).
    - Pure function: does not mutate any inputs.

    Args:
        nums1: First sequence of integers.
        nums2: Second sequence of integers.
        nums3: Third sequence of integers.
        nums4: Fourth sequence of integers.

    Returns:
        Total count of index tuples (i, j, k, l) whose sum is 0.

    Complexity:
        Time: O(len(nums1) * len(nums2) + len(nums3) * len(nums4)) -> O(n^2) when lengths are ~n.
        Space: O(len(nums1) * len(nums2)) for the pair sums hash table.

    Examples:
        >>> four_sum_ii([1, 2], [-2, -1], [-1, 2], [0, 2])
        2
        >>> four_sum_ii([0], [0], [0], [0])
        1
    """
    sum_counts: Counter[int] = Counter()
    for a in nums1:
        for b in nums2:
            sum_counts[a + b] += 1

    total_tuples = 0
    for c in nums3:
        for d in nums4:
            total_tuples += sum_counts[-(c + d)]

    return total_tuples
