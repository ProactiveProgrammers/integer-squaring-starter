"""Test suite to ensure that each function words correctly."""

from square import __version__

from square import main


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_compute_square_while_loop_positive():
    """Confirm that the while loop calculates squares correctly for positives."""
    value = 3
    square_value = main.compute_square_while(value)
    assert square_value == 9


def test_compute_square_while_loop_negative():
    """Confirm that the while loop calculates squares correctly for negatives."""
    value = -3
    square_value = main.compute_square_while(value)
    assert square_value == 9


def test_compute_square_for_loop_positive():
    """Confirm that the for loop calculates squares correctly for positives."""
    value = 3
    square_value = main.compute_square_for(value)
    assert square_value == 9


def test_compute_square_for_loop_negative():
    """Confirm that the for loop calculates squares correctly for negatives."""
    value = -3
    square_value = main.compute_square_for(value)
    assert square_value == 9


def test_compute_square_iterative_for_loop():
    """Confirm that the for loop calculates squares correctly for negatives and positives in loop."""
    number_list = """-72
        29
        61
        -42
        44"""
    square_function = main.compute_square_for
    square_list = main.compute_square_iterative(number_list, square_function)
    assert square_list == [72 * 72, 29 * 29, 61 * 61, 42 * 42, 44 * 44]


# TODO: Add a test case for confirming the correctness of the compute_square_iterative function
# when it is using the square_function as main.compute_square_while
