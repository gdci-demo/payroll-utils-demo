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
