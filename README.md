# sum-helpers

A modular, strictly-typed Python package providing pure algorithmic solutions for array sum and combination problems.

## Installation

```bash
pip install sum-helpers
```

## Features

- **Pure Functions**: Input collections are never mutated in-place.
- **Strictly Typed**: Full type annotations (`Sequence[int]`, `tuple[int, ...]`, `int | None`) supporting PEP 561 (`py.typed`).
- **Comprehensive Algorithms**: Includes two-pointer scans, hash-based lookups, bounding-based pruning, and recursive k-sum decomposition.

## Overview of Exported Functions

### 1. Two-Element Sums (`sum_helpers.two_sum`)
- `two_sum(nums, target)`: 0-indexed indices via single-pass hash map ($\mathcal{O}(n)$).
- `two_sum_sorted(numbers, target)`: 1-indexed two-pointer solution on sorted array ($\mathcal{O}(n)$ time, $\mathcal{O}(1)$ space).
- `two_sum_less_than_k(nums, k)`: Maximum sum strictly less than $k$ ($\mathcal{O}(n \log n)$).
- `two_sum_closest(nums, target)`: Pair sum closest to target ($\mathcal{O}(n \log n)$).
- `two_sum_unique_pairs(nums, target)`: All unique sorted pairs summing to target ($\mathcal{O}(n \log n)$).

### 2. Three-Element Sums (`sum_helpers.three_sum`)
- `three_sum(nums, target=0)`: All unique sorted triplets summing to target ($\mathcal{O}(n^2)$).
- `three_sum_closest(nums, target)`: Triplet sum closest to target ($\mathcal{O}(n^2)$).
- `three_sum_smaller(nums, target)`: Count index triplets with sum strictly less than target ($\mathcal{O}(n^2)$).

### 3. Triangle Sums (`sum_helpers.triangle`)
- `valid_triangle_number(nums)`: Count index triplets that can form a valid triangle ($\mathcal{O}(n^2)$).
- `is_valid_triangle(a, b, c)`: Geometric triangle inequality validator ($\mathcal{O}(1)$).
- `find_valid_triangles(nums)`: All unique sorted value triplets forming valid triangles ($\mathcal{O}(n^2)$).

### 4. Generalized K-Sum & Four Sum (`sum_helpers.k_sum`)
- `k_sum(nums, target, k)`: Generalized recursive two-pointer k-sum for arbitrary $k \ge 2$ ($\mathcal{O}(n^{k-1})$).
- `k_sum_closest(nums, target, k)`: Sum of $k$ integers closest to target ($\mathcal{O}(n^{k-1})$).
- `k_sum_smaller(nums, target, k)`: Count index $k$-tuples with sum strictly less than target ($\mathcal{O}(n^{k-1})$).
- `four_sum(nums, target=0)`: All unique 4-tuples summing to target ($\mathcal{O}(n^3)$).
- `four_sum_closest(nums, target)`: Sum of 4 integers closest to target ($\mathcal{O}(n^3)$).
- `four_sum_smaller(nums, target)`: Count index quadruplets with sum strictly less than target ($\mathcal{O}(n^3)$).
- `four_sum_ii(nums1, nums2, nums3, nums4)`: Count quadruplets across four separate arrays summing to 0 ($\mathcal{O}(n^2)$).

## Quickstart

```python
from sum_helpers import (
    two_sum,
    two_sum_sorted,
    two_sum_less_than_k,
    two_sum_closest,
    three_sum,
    three_sum_closest,
    three_sum_smaller,
    valid_triangle_number,
    k_sum,
    k_sum_closest,
    k_sum_smaller,
    four_sum,
    four_sum_closest,
    four_sum_smaller,
    four_sum_ii,
)

# Generalized K-Sum (k=4)
quadruplets = four_sum([1, 0, -1, 0, -2, 2], target=0)
assert quadruplets == [
    (-2, -1, 1, 2),
    (-2, 0, 0, 2),
    (-1, 0, 0, 1),
]

# Generalized K-Sum Closest (k=4)
assert four_sum_closest([1, 0, -1, 0, -2, 2], target=0) == 0

# Generalized K-Sum Smaller (k=4)
assert four_sum_smaller([1, 1, 1, 1], target=5) == 1

# Four Sum II across four independent lists
assert four_sum_ii([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
```

## Running Tests

```bash
uv run pytest -v
uv run pytest --doctest-modules src/
uv run --with mypy mypy src/ tests/
```

## Building for PyPI

```bash
uv build
uv publish
```
