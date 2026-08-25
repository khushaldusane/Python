"""
Module 6: Report Generator
Assembles the findings from business_metrics into a single
markdown summary report — mirrors the auto-report pattern used
in production reporting: raw data in, formatted business report out.
"""

import os
from datetime import datetime


def generate_markdown_report(findings: dict, churn_by_geo, churn_by_age,
                              revenue_risk, output_path: str):

    lines = []
    lines.append(f"# Bank Customer Churn & Risk Report")
    lines.append(f"_Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n")

    lines.append("## Executive Summary\n")
    lines.append(f"- **Overall churn rate:** {findings['overall_churn_rate_pct']}%")
    lines.append(
        f"- **Highest-churn geography:** {findings['highest_churn_geography']['geography']} "
        f"({findings['highest_churn_geography']['churn_rate_pct']}% churn)"
    )
    lines.append(
        f"- **Highest-churn age band:** {findings['highest_churn_age_band']['age_band']} "
        f"({findings['highest_churn_age_band']['churn_rate_pct']}% churn)"
    )
    lines.append(
        f"- **Inactive members churn at {findings['inactive_member_churn_pct']}%** vs "
        f"**{findings['active_member_churn_pct']}%** for active members"
    )
    lines.append(
        f"- **{findings['high_risk_customer_count']} customers ({findings['high_risk_pct_of_base']}% of base)** "
        f"flagged as High Risk by the rule-based scoring model\n"
    )

    lines.append("## Churn Rate by Geography\n")
    lines.append(churn_by_geo.to_markdown(index=False))
    lines.append("")

    lines.append("## Churn Rate by Age Band\n")
    lines.append(churn_by_age.to_markdown(index=False))
    lines.append("")

    lines.append("## Value at Risk by Risk Tier\n")
    lines.append(revenue_risk.to_markdown(index=False))
    lines.append("")

    lines.append("## Recommendations\n")
    lines.append(
        "1. **Prioritize re-engagement campaigns for inactive members** — "
        "this single factor shows the largest churn gap in the data.\n"
        "2. **Investigate the highest-churn geography** for service, pricing, or "
        "competitive factors specific to that region.\n"
        "3. **Target single-product customers with cross-sell offers** — "
        "low product engagement is a strong churn signal and is directly actionable.\n"
        "4. **Build a retention offer track for the High Risk tier** identified above, "
        "prioritized by value at risk rather than customer count alone."
    )

    report_text = "\n".join(lines)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(report_text)

    print(f"[report_generator] Report saved to {output_path}")
    return report_text