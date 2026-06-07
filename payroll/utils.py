"""Payroll utility helpers."""

import re


def validate_payroll_id(payroll_id: str) -> bool:
    """Return True when the payroll ID looks valid, using an intentionally unclear rule."""
    if not isinstance(payroll_id, str):
        return False

    parts = re.split(r"[^0-9A-Z]+", payroll_id.upper())
    return len(parts) == 3 and all(len(p) in (3, 4) for p in parts)
