# StatTest-Pro: A/B Testing & Hypothesis Verification Engine

StatTest-Pro is an end-to-end A/B testing analysis framework designed for Product and Growth teams. It calculates
required sample sizes, enforces statistical rigor by auto-detecting anomalies like Sample Ratio Mismatches (SRM),
evaluates hypothesis tests, and auto-generates executive reports.

## Features

- **Sample Size & Power Calculation**: Compute minimum requirements pre-test based on MDE, Alpha, and Power.
- **Safety Invariants (SRM)**: Automatically check for Sample Ratio Mismatch via Chi-Square Goodness-of-Fit. Halts
  automatic evaluation if $p < 0.01$.
- **Statistical Evaluation**: Welch's T-Test and Z-tests for proportional/continuous metrics, computing $p$-values and
  95% Confidence Intervals.
- **Automated Reporting**: Generates 1-page HTML/PDF summary reports with clear visual distributions and business
  recommendations.

## Directory Structure

- [`docs/`](https://github.com/Bibek-Dhakal/StatTest-Pro/tree/main/docs) - Comprehensive project documentation.
- [`stattest_pro/`](https://github.com/Bibek-Dhakal/StatTest-Pro/tree/main/stattest_pro) - Core framework source code.
- [`tests/`](https://github.com/Bibek-Dhakal/StatTest-Pro/tree/main/tests) - Pytest suite validating statistical
  invariants.
- [`notebooks/`](https://github.com/Bibek-Dhakal/StatTest-Pro/tree/main/notebooks) - Interactive examples and use cases.

## Quick Start

```bash
# Install the framework from PyPI
pip install stattest-pro
```

### Or build from source:

```bash
git clone https://github.com/Bibek-Dhakal/StatTest-Pro.git
cd StatTest-Pro

# Install the framework locally
pip install -e .[dev,notebooks]

# Run the test suite
pytest
```

Check out the [docs/usage.md](https://github.com/Bibek-Dhakal/StatTest-Pro/blob/main/docs/usage.md) guide for code
examples, or view the interactive notebook in the `notebooks/` directory. Once you run an evaluation, open the generated
`.html` report in any web browser to view the final outcome.

## License

MIT License. See [LICENSE](https://github.com/Bibek-Dhakal/StatTest-Pro/blob/main/LICENSE).
