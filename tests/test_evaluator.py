import pytest

from stattest_pro.evaluator import evaluate_conversion


def test_evaluate_conversion_significant():
    # Large n, clear difference
    results = evaluate_conversion(
        conversions_a=1000,
        total_a=10000,  # 10%
        conversions_b=1200,
        total_b=10000,  # 12%
        alpha=0.05,
        mde=0.015,
    )

    assert results["significant"] is True
    assert results["p_value"] < 0.05
    assert results["relative_lift"] == pytest.approx(0.20)
    assert "Launch" in results["decision"]


def test_evaluate_conversion_insignificant():
    # Small n, unclear difference
    results = evaluate_conversion(
        conversions_a=10,
        total_a=100,  # 10%
        conversions_b=11,
        total_b=100,  # 11%
        alpha=0.05,
        mde=0.02,
    )

    assert results["significant"] is False
    assert results["p_value"] > 0.05
    assert "Inconclusive" in results["decision"]
