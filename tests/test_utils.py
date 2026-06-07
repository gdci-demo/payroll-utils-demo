from payroll.utils import is_valid_payroll_id


def test_valid_payroll_id_returns_true():
    assert is_valid_payroll_id("ABC-1234-XYZ") is True


def test_lowercase_or_malformed_payroll_id_returns_false():
    assert is_valid_payroll_id("abc-1234-xyz") is False
    assert is_valid_payroll_id("AB-123-XYZ-999") is False
