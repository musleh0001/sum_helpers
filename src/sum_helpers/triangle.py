"""Triangle Sum and Valid Triangle helper functions.

This module provides helpers for triangle inequality and sum problems:
- LC 611: Valid Triangle Number (count triplets that can form sides of a triangle)
- is_valid_triangle: Check whether three side lengths can form a valid triangle
- find_valid_triangles: Return unique sorted value triplets forming valid triangles
"""

from __future__ import annotations

from typing import Sequence

__all__ = [
    "valid_triangle_number",
    "is_valid_triangle",
    "find_valid_triangles",
]


def is_valid_triangle(a: int, b: int, c: int) -> bool:
    """Check if three side lengths can form a valid, non-degenerate triangle.

    A valid triangle requires strictly positive side lengths and must satisfy the
    triangle inequality theorem:
    a + b > c and a + c > b and b + c > a.

    Args:
        a: First side length.
        b: Second side length.
        c: Third side length.

    Returns:
        True if the sides form a valid non-degenerate triangle, False otherwise.

    Complexity:
        Time: O(1)
        Space: O(1)

    Examples:
        >>> is_valid_triangle(3, 4, 5)
        True
        >>> is_valid_triangle(1, 2, 3)
        False
        >>> is_valid_triangle(0, 2, 2)
        False
        >>> is_valid_triangle(-2, 3, 4)
        False
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)


def valid_triangle_number(nums: Sequence[int]) -> int:
    """Count the number of triplets that can form a valid triangle (LeetCode 611).

    Assumptions & Behavior:
    - Input can be unsorted and may contain zero or negative numbers (which cannot
      form triangle sides).
    - Counts index triplets (i, j, k) with i < j < k whose elements can form a triangle.
    - Two-pointer method: sorts array, fixes the largest side k from right to left,
      and finds pairs (left, right) where nums[left] + nums[right] > nums[k].
    - Pure function: does not mutate caller's input sequence.

    Args:
        nums: A sequence of side lengths.

    Returns:
        Total number of index triplets (i, j, k) with i < j < k that can form a triangle.

    Complexity:
        Time: O(n^2) where n is len(nums).
        Space: O(n) for the sorted copy.

    Examples:
        >>> valid_triangle_number([2, 2, 3, 4])
        3
        >>> valid_triangle_number([4, 2, 3, 4])
        4
        >>> valid_triangle_number([0, 1, 0])
        0
        >>> valid_triangle_number([7, 0, 0, 0])
        0
    """
    n = len(nums)
    if n < 3:
        return 0

    sorted_nums = sorted(nums)
    count = 0

    # Iterate from the largest side backwards down to index 2
    for k in range(n - 1, 1, -1):
        c = sorted_nums[k]
        # In sorted array, if the largest side is <= 0, no valid triangle can be formed
        if c <= 0:
            break

        left = 0
        right = k - 1

        while left < right:
            if sorted_nums[left] + sorted_nums[right] > c:
                # Since sorted_nums is non-decreasing, all elements between left and right - 1
                # added to sorted_nums[right] will also be > c.
                count += right - left
                right -= 1
            else:
                left += 1

    return count


def find_valid_triangles(nums: Sequence[int]) -> list[tuple[int, int, int]]:
    """Return all unique value triplets (a, b, c) with a <= b <= c that form a valid triangle.

    Unlike valid_triangle_number which counts index combinations, this function returns
    the set of distinct side-length combinations that can form valid triangles.

    Assumptions & Behavior:
    - Side lengths must be positive (<= 0 sides are filtered out).
    - Triplets are unique (deduplicated).
    - Each triplet (a, b, c) is sorted such that a <= b <= c.
    - Pure function: does not mutate caller's input.

    Args:
        nums: A sequence of integers representing candidate side lengths.

    Returns:
        A list of unique sorted tuples (a, b, c) where a + b > c.

    Complexity:
        Time: O(n^2) where n is len(nums).
        Space: O(n) for sorting and deduplication.

    Examples:
        >>> find_valid_triangles([2, 2, 3, 4])
        [(2, 2, 3), (2, 3, 4)]
        >>> find_valid_triangles([1, 2, 3])
        []
    """
    # Filter positive sides only and sort
    positive_sides = sorted([x for x in nums if x > 0])
    n = len(positive_sides)
    if n < 3:
        return []

    unique_triplets: set[tuple[int, int, int]] = set()

    for k in range(n - 1, 1, -1):
        c = positive_sides[k]
        left = 0
        right = k - 1

        while left < right:
            if positive_sides[left] + positive_sides[right] > c:
                for i in range(left, right):
                    unique_triplets.add((positive_sides[i], positive_sides[right], c))
                right -= 1
            else:
                left += 1

    return sorted(unique_triplets)
