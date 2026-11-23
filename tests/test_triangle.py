"""Tests for triangle module."""

from sum_helpers.triangle import (
    find_valid_triangles,
    is_valid_triangle,
    valid_triangle_number,
)


class TestTriangleHelpers:
    def test_is_valid_triangle_truthy(self) -> None:
        assert is_valid_triangle(3, 4, 5) is True
        assert is_valid_triangle(2, 2, 3) is True
        assert is_valid_triangle(5, 5, 5) is True

    def test_is_valid_triangle_falsy(self) -> None:
        assert is_valid_triangle(1, 2, 3) is False  # degenerate (1 + 2 == 3)
        assert is_valid_triangle(1, 2, 5) is False
        assert is_valid_triangle(0, 5, 5) is False
        assert is_valid_triangle(-3, 4, 5) is False


class TestValidTriangleNumber:
    def test_standard_cases(self) -> None:
        assert valid_triangle_number([2, 2, 3, 4]) == 3
        assert valid_triangle_number([4, 2, 3, 4]) == 4

    def test_equilateral_triplets(self) -> None:
        assert valid_triangle_number([3, 3, 3]) == 1
        assert valid_triangle_number([3, 3, 3, 3]) == 4

    def test_with_zeros_and_negatives(self) -> None:
        assert valid_triangle_number([0, 1, 0]) == 0
        assert valid_triangle_number([7, 0, 0, 0]) == 0
        assert valid_triangle_number([-2, -1, 3, 4, 5]) == 1  # only (3, 4, 5)

    def test_short_inputs(self) -> None:
        assert valid_triangle_number([]) == 0
        assert valid_triangle_number([1]) == 0
        assert valid_triangle_number([1, 2]) == 0

    def test_immutability(self) -> None:
        nums = [4, 2, 3, 4]
        copy = list(nums)
        valid_triangle_number(nums)
        assert nums == copy


class TestFindValidTriangles:
    def test_standard_case(self) -> None:
        nums = [2, 2, 3, 4]
        res = find_valid_triangles(nums)
        assert res == [(2, 2, 3), (2, 3, 4)]

    def test_no_valid_triangles(self) -> None:
        assert find_valid_triangles([1, 2, 3]) == []

    def test_filters_zeros_and_negatives(self) -> None:
        nums = [0, -5, 3, 4, 5]
        assert find_valid_triangles(nums) == [(3, 4, 5)]

    def test_short_inputs(self) -> None:
        assert find_valid_triangles([]) == []
        assert find_valid_triangles([1, 2]) == []
