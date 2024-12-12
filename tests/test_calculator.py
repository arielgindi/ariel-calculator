import pytest
from calculator.expression_calculator import calculate_expression

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

def test_factorial_followed_by_subtraction():
    assert calculate_expression("9! - 8") == 362872

def test_factorial_subtraction_between_factorials():
    assert calculate_expression("9! - 8!") == 322560

def test_factorial_followed_by_double_minus_number():
    assert calculate_expression("9! - -8") == 362888

def test_sign_simplification_complex():
    assert calculate_expression("---+++-++-10") == -10

def test_tilde_on_factorial_in_parentheses():
    assert calculate_expression("~(10!)") == -3628800

def test_tilde_on_factorial_invalid():
    with pytest.raises(ValueError):
        calculate_expression("~10!")

def test_nested_tilde_with_parentheses():
    assert calculate_expression("-(~(+10))") == 10

def test_signs_with_tilde():
    assert calculate_expression("-+~+10") == 10

def test_double_tilde_no_parentheses():
    with pytest.raises(ValueError):
        calculate_expression("~~3")

def test_double_tilde_with_parentheses():
    assert calculate_expression("~(~3)") == 3

def test_plus_tilde_minus():
    assert calculate_expression("3+~-3") == 6

def test_simple_factorial():
    assert calculate_expression("3!") == 6

def test_factorial_after_negative():
    assert calculate_expression("-10!") == -3628800

def test_tilde_minus_combination_1():
    # ~4-~-10^2 should result in -104
    assert calculate_expression("~4-~-10^2") == -104

def test_tilde_minus_combination_2():
    # ~4--~10^2 should result in 96
    assert calculate_expression("~4--~10^2") == 96
