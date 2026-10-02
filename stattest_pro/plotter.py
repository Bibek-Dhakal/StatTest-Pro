import base64
import io

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns


def generate_conversion_plot_base64(results: dict) -> str:
    """
    Generates a simple bar chart with error bars representing the 95% CI
    and returns it as a base64 string for HTML embedding.
    """
    sns.set_theme(style="whitegrid")

    rates = [results["rate_a"], results["rate_b"]]

    # Error margins calculation: (upper_ci - rate)
    err_a = results["ci_a"][1] - results["rate_a"]
    err_b = results["ci_b"][1] - results["rate_b"]
    errors = [err_a, err_b]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(
        ["Control (A)", "Variant (B)"],
        rates,
        yerr=errors,
        capsize=10,
        color=["#3498db", "#2ecc71"],
        alpha=0.8,
    )

    ax.set_ylabel("Conversion Rate")
    ax.set_title("Experiment Conversion Rates with 95% CI")

    # Safely format y-axis to percentage without triggering UserWarning
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=1))

    plt.tight_layout()

    # Render to base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=150)
    plt.close(fig)

    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
