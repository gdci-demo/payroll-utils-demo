"""Payroll utility helpers."""

import re


def is_valid_payroll_id(payroll_id: str) -> bool:
    """Return True when a payroll ID matches the exact allowed format.

    A valid payroll ID must be:
    - 3 uppercase letters
    - a hyphen
    - 4 digits
    - a hyphen
    - 2 or 3 uppercase letters
    """
    if not isinstance(payroll_id, str):
        return False

    return bool(re.fullmatch(r"[A-Z]{3}-\d{4}-[A-Z]{2,3}", payroll_id))


def is_valid_bank_account(account_number: str) -> bool:
    """Return True when an account number is valid for payroll direct deposit.

    A valid bank account number is a string containing 9 to 17 digits.
    """
    if not isinstance(account_number, str):
        return False

    return bool(re.fullmatch(r"\d{9,17}", account_number))


def is_string_valid(value: str) -> bool:
    """Return True when a string is non-empty after stripping whitespace."""
    if not isinstance(value, str):
        return False

    return bool(value.strip())


def calculate_net_pay(gross_pay: float, tax_rate: float = 0.2, deductions: float = 0.0) -> float:
    """Calculate a simple net pay amount for payroll processing.

    Net pay is calculated as gross pay minus payroll tax and other deductions.
    """
    if not isinstance(gross_pay, (int, float)):
        raise TypeError("gross_pay must be a number")
    if not isinstance(tax_rate, (int, float)):
        raise TypeError("tax_rate must be a number")
    if not isinstance(deductions, (int, float)):
        raise TypeError("deductions must be a number")

    if gross_pay < 0:
        raise ValueError("gross_pay must not be negative")
    if not (0.0 <= tax_rate <= 1.0):
        raise ValueError("tax_rate must be between 0.0 and 1.0")
    if deductions < 0:
        raise ValueError("deductions must not be negative")

    taxable_amount = gross_pay * tax_rate
    return round(gross_pay - taxable_amount - deductions, 2)
