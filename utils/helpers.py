"""
Helper functions for hng12-stage-1
-----------------------------------

This module provides utility functions the hng12-stage-1 module.

Functions:
- odd_even -> str: Check if a number is odd or even.
- is_perfect -> bool: Check if a number is perfect.
- digit_sum -> int: Calculate the sum of digits of a number.
- is_prime(num) -> bool: Check if a number is prime.
- is_armstrong -> str: Check if a number is an Armstrong number.

-----------------------------------
Author: Mohamed Ali
"""

import math


def odd_even(num):
    """Check whether a number is even or odd"""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def is_perfect(num):
    """Checks if a number is perfect"""
    if num < 1:
        return False

    divisor_sum = sum(i for i in range(1, num) if num % 1 == 0)
    return divisor_sum == num


def digit_sum(num):
    """Calculates the sum of digit in a number"""
    return sum(int(digit) for digit in str(num))


def is_prime(num):
    """Checks whether a number is prime or not"""
    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


def is_armstrong(num):
    """Checks if a number is an armstrong"""
    digits = len(str(num))
    total = sum(int(digit) ** digits for digit in str(num))

    if total == num:
        return "armstrong"
