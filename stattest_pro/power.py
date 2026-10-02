import math

import statsmodels.stats.api as sms


def calculate_sample_size(
    baseline_rate: float, mde: float, alpha: float = 0.05, power: float = 0.80
) -> int:
    """
    Calculates minimum sample size per variant for a proportion metric.

    Args:
        baseline_rate: Expected baseline conversion rate (e.g., 0.10 for 10%).
        mde: Minimum Detectable Effect in absolute terms (e.g., 0.02 for +2%).
        alpha: Statistical significance level (Type I error rate).
        power: Statistical power (1 - Type II error rate).

    Returns:
        Required sample size per variant (integer).
    """
    effect_size = sms.proportion_effectsize(baseline_rate, baseline_rate + mde)
    required_n = sms.NormalIndPower().solve_power(effect_size, power=power, alpha=alpha, ratio=1.0)
    return math.ceil(required_n)
