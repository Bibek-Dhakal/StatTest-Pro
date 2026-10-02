import numpy as np
from statsmodels.stats.proportion import proportion_confint, proportions_ztest


def evaluate_conversion(
    conversions_a: int,
    total_a: int,
    conversions_b: int,
    total_b: int,
    alpha: float = 0.05,
    mde: float = 0.0,
) -> dict:
    """
    Evaluates statistical significance between two conversion rates.

    Args:
        conversions_a: Successes in control.
        total_a: Total observations in control.
        conversions_b: Successes in treatment.
        total_b: Total observations in treatment.
        alpha: Significance level.
        mde: The predetermined Minimum Detectable Effect (absolute).

    Returns:
        Dictionary containing metric statistics, p-value, and final recommendation.
    """
    count = np.array([conversions_b, conversions_a])
    nobs = np.array([total_b, total_a])

    # Two-sided Z-test for proportions
    stat, pval = proportions_ztest(count, nobs)

    # 95% Confidence Intervals
    ci_low_b, ci_upp_b = proportion_confint(conversions_b, total_b, alpha=alpha, method="normal")
    ci_low_a, ci_upp_a = proportion_confint(conversions_a, total_a, alpha=alpha, method="normal")

    rate_a = conversions_a / total_a if total_a > 0 else 0
    rate_b = conversions_b / total_b if total_b > 0 else 0
    lift = (rate_b - rate_a) / rate_a if rate_a > 0 else 0
    absolute_diff = rate_b - rate_a

    is_significant = pval < alpha
    exceeds_mde = absolute_diff >= mde

    if is_significant and exceeds_mde:
        decision = "Launch (Statistically significant and exceeds MDE)"
    elif is_significant and absolute_diff > 0:
        decision = "Iterate (Significant but positive impact is below target MDE)"
    elif is_significant and absolute_diff < 0:
        decision = "Roll Back (Statistically significant negative impact)"
    else:
        decision = "Inconclusive (No statistical significance detected)"

    return {
        "metric_type": "proportion",
        "rate_a": rate_a,
        "rate_b": rate_b,
        "relative_lift": lift,
        "absolute_diff": absolute_diff,
        "p_value": float(pval),
        "significant": bool(is_significant),
        "ci_a": (float(ci_low_a), float(ci_upp_a)),
        "ci_b": (float(ci_low_b), float(ci_upp_b)),
        "decision": decision,
        "alpha": alpha,
        "mde": mde,
    }
