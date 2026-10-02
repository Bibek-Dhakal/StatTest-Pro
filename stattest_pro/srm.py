from scipy.stats import chisquare


class SRMError(Exception):
    """Raised when a Sample Ratio Mismatch is detected."""

    pass


def check_srm(
    users_a: int, users_b: int, expected_ratio: float = 1.0, threshold_p: float = 0.01
) -> float:
    """
    Checks for Sample Ratio Mismatch (SRM) using a Chi-Square Goodness-of-Fit test.

    Args:
        users_a: Traffic observed in variant A.
        users_b: Traffic observed in variant B.
        expected_ratio: Expected split ratio (A/B). Default is 1.0 (50/50 split).
        threshold_p: P-value threshold to flag SRM. Standard is 0.01.

    Returns:
        The computed p-value.

    Raises:
        SRMError: If the p-value is below the threshold.
    """
    total = users_a + users_b
    expected_a = total * (expected_ratio / (1 + expected_ratio))
    expected_b = total * (1 / (1 + expected_ratio))

    _, p_value = chisquare([users_a, users_b], f_exp=[expected_a, expected_b])

    if p_value < threshold_p:
        raise SRMError(
            f"SRM Detected! Traffic split anomaly. p-value ({p_value:.4f}) < {threshold_p}. "
            "Primary metric evaluations are invalidated."
        )

    return float(p_value)
