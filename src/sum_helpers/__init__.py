"""sum_helpers: Clean, modular, well-typed Python helpers for sum and combination problems.

Core modules:
- two_sum:
    - two_sum (LC 1)
    - two_sum_sorted (LC 167)
    - two_sum_less_than_k (LC 1099)
    - two_sum_closest
    - two_sum_unique_pairs

- three_sum:
    - three_sum (LC 15)
    - three_sum_closest (LC 16)
    - three_sum_smaller (LC 259)

- triangle:
    - valid_triangle_number (LC 611)
    - is_valid_triangle
    - find_valid_triangles

- k_sum:
    - k_sum (Generalized arbitrary k >= 2)
    - k_sum_closest
    - k_sum_smaller
    - four_sum (LC 18)
    - four_sum_closest
    - four_sum_smaller
    - four_sum_ii (LC 454)
"""

from __future__ import annotations

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
from sum_helpers.triangle import (
    find_valid_triangles,
    is_valid_triangle,
    valid_triangle_number,
)
from sum_helpers.two_sum import (
    two_sum,
    two_sum_closest,
    two_sum_less_than_k,
    two_sum_sorted,
    two_sum_unique_pairs,
)

__all__ = [
    # Two sum
    "two_sum",
    "two_sum_sorted",
    "two_sum_less_than_k",
    "two_sum_closest",
    "two_sum_unique_pairs",
    # Three sum
    "three_sum",
    "three_sum_closest",
    "three_sum_smaller",
    # Triangle sum
    "valid_triangle_number",
    "is_valid_triangle",
    "find_valid_triangles",
    # K-sum & Four sum
    "k_sum",
    "k_sum_closest",
    "k_sum_smaller",
    "four_sum",
    "four_sum_closest",
    "four_sum_smaller",
    "four_sum_ii",
]

__version__ = "0.1.0"
