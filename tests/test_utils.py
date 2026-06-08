from payroll.utils import calculate_net_pay, is_valid_bank_account, is_valid_payroll_id


def test_valid_payroll_id_returns_true():
    assert is_valid_payroll_id("ABC-1234-XYZ") is True


def test_lowercase_or_malformed_payroll_id_returns_false():
    assert is_valid_payroll_id("abc-1234-xyz") is False
    assert is_valid_payroll_id("AB-123-XYZ-999") is False


def test_valid_bank_account_returns_true_for_valid_digits():
    assert is_valid_bank_account("123456789") is True
    assert is_valid_bank_account("00012345678901234") is True


def test_invalid_bank_account_returns_false_for_bad_values():
    assert is_valid_bank_account("12345") is False
    assert is_valid_bank_account("acct-123456") is False
    assert is_valid_bank_account(123456789) is False


def test_calculate_net_pay_computes_expected_amount():
    assert calculate_net_pay(5000.00, tax_rate=0.22, deductions=150.00) == 3750.0
    assert calculate_net_pay(1000.0, tax_rate=0.1, deductions=0.0) == 900.0


def test_calculate_net_pay_validates_inputs():
    try:
        calculate_net_pay(-1000.0, tax_rate=0.2, deductions=0)
        assert False, "Expected ValueError for negative gross pay"
    except ValueError:
        pass

    try:
        calculate_net_pay(1000.0, tax_rate=1.5, deductions=0)
        assert False, "Expected ValueError for invalid tax rate"
    except ValueError:
        pass

    try:
        calculate_net_pay(1000.0, tax_rate=0.2, deductions=-50.0)
        assert False, "Expected ValueError for negative deductions"
    except ValueError:
        pass
