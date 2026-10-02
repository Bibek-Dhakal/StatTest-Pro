# 🚀 Usage Guide

This guide details how to implement A/B tests using StatTest-Pro.

[← Back to Documentation Index](README.md)

## End-to-End Workflow Example

```python
from stattest_pro.power import calculate_sample_size
from stattest_pro.srm import check_srm, SRMError
from stattest_pro.evaluator import evaluate_conversion
from stattest_pro.reporter import generate_report

# 1. Pre-Test: Power Calculation
required_n = calculate_sample_size(baseline_rate=0.05, mde=0.01, alpha=0.05, power=0.80)
print(f"Required Sample Size per variant: {required_n}")

# 2. Post-Test Data Ingestion
total_a, conversions_a = 50000, 2500
total_b, conversions_b = 50100, 2800

# 3. Safety Check: Sample Ratio Mismatch (SRM)
try:
    check_srm(total_a, total_b, expected_ratio=1.0)
except SRMError as e:
    print(f"Halt! {e}")
    exit(1)

# 4. Evaluation
results = evaluate_conversion(conversions_a, total_a, conversions_b, total_b)

# 5. Reporting
html_path = generate_report(results, output_file="experiment_results.html")
print(f"Report generated at {html_path}. Open this file in your web browser to view the outcome.")
```

## Environment Variables
The `.env` file handles project defaults. Create one by copying `.env.example`.

| Name | Type | Default Value | Description |
|------|------|---------------|-------------|
| `DEFAULT_ALPHA` | Float | 0.05 | Default significance level. |
| `DEFAULT_POWER` | Float | 0.80 | Default statistical power target. |
| `DEFAULT_MDE` | Float | 0.02 | Minimum Detectable Effect threshold. |
| `REPORT_OUTPUT_DIR` | String | `./reports` | Where HTML reports are saved. |
