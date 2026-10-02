import os

from jinja2 import BaseLoader, Environment

from stattest_pro.plotter import generate_conversion_plot_base64

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>A/B Test Executive Report</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1, h2 { color: #2c3e50; }
        .card { border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; }
        .metric-grid { display: flex; justify-content: space-between; flex-wrap: wrap; }
        .metric { width: 45%; margin-bottom: 15px; }
        .value { font-size: 24px; font-weight: bold; color: #2980b9; }
        .decision-highlight { font-size: 18px; font-weight: bold; color: #fff; background-color: #2c3e50; padding: 10px; border-radius: 5px; text-align: center;}
        img { max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; }
    </style>
</head>
<body>
    <h1>A/B Test Executive Summary</h1>

    <div class="decision-highlight">
        Recommendation: {{ results.decision }}
    </div>

    <div class="card">
        <h2>Key Metrics</h2>
        <div class="metric-grid">
            <div class="metric">
                <div>Control Conversion Rate</div>
                <div class="value">{{ "{:.2%}".format(results.rate_a) }}</div>
                <small>95% CI: [{{ "{:.2%}".format(results.ci_a[0]) }}, {{ "{:.2%}".format(results.ci_a[1]) }}]</small>
            </div>
            <div class="metric">
                <div>Variant Conversion Rate</div>
                <div class="value">{{ "{:.2%}".format(results.rate_b) }}</div>
                <small>95% CI: [{{ "{:.2%}".format(results.ci_b[0]) }}, {{ "{:.2%}".format(results.ci_b[1]) }}]</small>
            </div>
            <div class="metric">
                <div>Relative Lift</div>
                <div class="value">{{ "{:.2%}".format(results.relative_lift) }}</div>
            </div>
            <div class="metric">
                <div>P-Value</div>
                <div class="value">{{ "{:.4f}".format(results.p_value) }}</div>
                <small>Significant at alpha={{ results.alpha }}? <strong>{{ results.significant }}</strong></small>
            </div>
        </div>
    </div>

    <div class="card">
        <h2>Distribution Visualization</h2>
        <img src="data:image/png;base64,{{ plot_base64 }}" alt="Conversion Plot">
    </div>
</body>
</html>
"""


def generate_report(results: dict, output_file: str = "report.html") -> str:
    """
    Generates a standalone HTML report summarizing the A/B test results.
    """
    env = Environment(loader=BaseLoader())
    template = env.from_string(HTML_TEMPLATE)

    plot_b64 = generate_conversion_plot_base64(results)

    html_content = template.render(results=results, plot_base64=plot_b64)

    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    return os.path.abspath(output_file)
