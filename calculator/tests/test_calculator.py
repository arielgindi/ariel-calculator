import pytest

from calculator.core.expression_calculator import calculate_expression


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
    with pytest.raises(ValueError):
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

def test_tilde_minus_combination_2():
    with pytest.raises(ValueError):
        assert calculate_expression("~4--~10^2") == 96


def test_parentheses_tilde_minus_combination():
    with pytest.raises(ValueError):
        assert calculate_expression("(5 + 8 ) - - ~9") == 4


def test_tilde_on_factorial_with_average():
    # 9! = 362,880
    # ~(9!) = -362,880
    # (-362,880 @ 3) = (-362,880+3)/2 = (-362,877)/2 = -181438.5
    assert calculate_expression("~(9!)@3") == -181438.5


def test_complex_precedence_mix():
    assert calculate_expression("3! - ~-10^2 @5*2 + ~4 &9") == -6322.555320336759


# '#' operator tests:
def test_sum_digits_1():
    # 123# = 6
    assert calculate_expression("123#") == 6


def test_sum_digits_2():
    # 99## -> 99#=18, 18#=9
    assert calculate_expression("99##") == 9


def test_sum_digits_3():
    # 2.3# = 2+3=5
    assert calculate_expression("2.3#") == 5


def test_sum_digits_4():
    # -123# = -(1+2+3)= -6
    assert calculate_expression("-123#") == -6


# New Tests

def test_expr_3_plus_tilde_minus_3():
    assert calculate_expression("3+~-3") == 6


def test_expr_tilde_minus_3_factorial():
    assert calculate_expression("~-3!") == 6


def test_expr_tilde_minus_minus_3_factorial():
    with pytest.raises(ValueError):
        calculate_expression("~--3!")


def test_expr_minus_minus_tilde_minus_minus_3():
    with pytest.raises(ValueError):
        calculate_expression("--~--3")


def test_expr_tilde_minus_minus_tilde_minus_3():
    with pytest.raises(ValueError):
        calculate_expression("~--~-3")


def test_expr_double_tilde_3_again():
    with pytest.raises(ValueError):
        calculate_expression("~~3")


def test_expr_2_minus_minus_3_factorial():
    with pytest.raises(ValueError):
        calculate_expression("2 - - 3!")


def test_expr_minus_3_factorial():
    assert calculate_expression("-3!") == -6


def test_expr_minus_minus_3_factorial():
    assert calculate_expression("--3!") == 6


def test_expr_2_minus_minus_minus_3_factorial():
    assert calculate_expression("2---3!") == -4


def test_expr_2_plus_minus_minus_3_factorial():
    assert calculate_expression("2 +--3!") == 8


def test_unary_minus_power_precedence():
    assert calculate_expression("-2 ^ 3") == -8


def test_multiple_space_between_number():
    with pytest.raises(ValueError):
        calculate_expression("123 456")


def test_unary_parenthesized_number_factorial():
    assert calculate_expression("2---(1+1+1)!") == -4


def test_large_number_precision():
    assert str(calculate_expression("4444444444444444444444444444444.000000")) == "4444444444444444444444444444444"
