from stattest_pro.power import calculate_sample_size


def test_calculate_sample_size():
    # Given a baseline of 10% and looking for a 2% absolute increase (to 12%)
    # with 5% alpha and 80% power.
    required_n = calculate_sample_size(baseline_rate=0.10, mde=0.02, alpha=0.05, power=0.80)

    # Standard theoretical calculation expects ~3922 or ~3923 depending on approximation method.
    assert 3800 < required_n < 4100
