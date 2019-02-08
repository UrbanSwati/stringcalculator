import pytest
from app import get_operator, calculate_string
import operator


class TestOperatorStringConvert:
    def test_add_operator(self):
        assert get_operator("Add") == operator.add

    def test_subtract_operator(self):
        assert get_operator("Subtract") == operator.sub

    def test_multiply_operator(self):
        assert get_operator("multiply") == operator.mul

    def test_divide_operator(self):
        assert get_operator("divide") == operator.truediv

    def test_square_root_operator(self):
        assert get_operator("square_root") == operator.pow


class TestStringCalculator:
    def test_add_calculation(self):
        assert calculate_string("1,2,3,4", "add") == 10
        assert calculate_string("2,2,2,2,2,2", "ADD") == 12

    def test_subtract_calculation(self):
        assert calculate_string("10,2,2,2", "subtract") == 4

    def test_multiply_calculation(self):
        assert calculate_string("2,2,2", "Multiply") == 8
        assert calculate_string("1,1,1,1", "Multiply") == 1
        assert calculate_string("5,5,5,5", "Multiply") == 625

    def test_divide_calculation(self):
        assert calculate_string("100,2,2", "divide") == 25

    def test_square_root_calculation(self):
        assert calculate_string("","square_root") == 0
