import pytest
from calculator.expression_evaluator import calculate_expression

def test_empty_expression():
    with pytest.raises(ValueError):
        calculate_expression("")

def test_garbage_input():
    with pytest.raises(ValueError):
        calculate_expression("abc")

def test_simple_add():
    assert calculate_expression("3+5") == 8

def test_factorial():
    assert calculate_expression("3!") == 6

def test_unary_minus():
    assert calculate_expression("-3+7") == 4

def test_multiple_unary_minus_complex():
    assert calculate_expression("2---3!") == -4

def test_tilde_multiple_unary_minus_factorial():
    with pytest.raises(ValueError):
        calculate_expression("~--3!")

def test_plus_multiple_unary_minus_factorial():
    assert calculate_expression("2 +--3!") == 8

def test_complex_power():
    with pytest.raises(ValueError):
        calculate_expression("(2---3!)^((~--3!)@5)")

def test_complicated_precedence_no_parentheses():
    assert calculate_expression("3+5*2^2-4/2") == 21