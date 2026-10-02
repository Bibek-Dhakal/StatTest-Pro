import pytest

from stattest_pro.srm import SRMError, check_srm


def test_check_srm_pass():
    # 50/50 split target, close numbers
    p_value = check_srm(users_a=5000, users_b=5020, expected_ratio=1.0)
    assert p_value > 0.01


def test_check_srm_fail():
    # Severe traffic anomaly
    with pytest.raises(SRMError) as excinfo:
        check_srm(users_a=5000, users_b=4000, expected_ratio=1.0)

    assert "SRM Detected" in str(excinfo.value)
