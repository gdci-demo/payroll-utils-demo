"""Payroll utility helpers."""

import re


def is_valid_payroll_id(payroll_id: str) -> bool:
    """Return True when a payroll ID contains exactly three alphanumeric groups.

    The input is normalized to uppercase and split on any non-alphanumeric separator.
    A valid payroll ID has three groups, and each group must be 3 or 4 characters long.
    """
    if not isinstance(payroll_id, str):
        return False

    normalized_id = payroll_id.upper()
    groups = re.split(r"[^0-9A-Z]+", normalized_id)
    return len(groups) == 3 and all(len(group) in (3, 4) for group in groups)
