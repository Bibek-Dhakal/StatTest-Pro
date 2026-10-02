# StatTest-Pro: A/B Testing & Hypothesis Verification Engine

StatTest-Pro is an end-to-end A/B testing analysis framework designed for Product and Growth teams. It calculates required sample sizes, enforces statistical rigor by auto-detecting anomalies like Sample Ratio Mismatches (SRM), evaluates hypothesis tests, and auto-generates executive reports.

## Features
- **Sample Size & Power Calculation**: Compute minimum requirements pre-test based on MDE, Alpha, and Power.
- **Safety Invariants (SRM)**: Automatically check for Sample Ratio Mismatch via Chi-Square Goodness-of-Fit. Halts automatic evaluation if $p < 0.01$.
- **Statistical Evaluation**: Welch's T-Test and Z-tests for proportional/continuous metrics, computing $p$-values and 95% Confidence Intervals.
- **Automated Reporting**: Generates 1-page HTML/PDF summary reports with clear visual distributions and business recommendations.

## Directory Structure
- [`docs/`](docs/README.md) - Comprehensive project documentation.
- [`stattest_pro/`](stattest_pro/) - Core framework source code.
- [`tests/`](tests/) - Pytest suite validating statistical invariants.
- [`notebooks/`](notebooks/) - Interactive examples and use cases.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/StatTest-Pro.git
cd StatTest-Pro

# Install the framework
pip install -e .[dev,notebooks]

# Run the test suite
pytest
```

Check out the [docs/usage.md](docs/usage.md) guide for code examples, or view the interactive notebook in the `notebooks/` directory. Once you run an evaluation, open the generated `.html` report in any web browser to view the final outcome.

## License
MIT License. See [LICENSE](LICENSE).
