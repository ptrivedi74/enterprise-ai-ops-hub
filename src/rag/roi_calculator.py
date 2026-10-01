def calculate_monthly_roi(manual_hours: float, hourly_rate: float, daily_tokens: int,
                          token_cost_per_1k: float = 0.002) -> dict:
    monthly_manual_cost = manual_hours * hourly_rate * 22
    monthly_token_cost = (daily_tokens / 1000) * token_cost_per_1k * 22
    net_savings = monthly_manual_cost - monthly_token_cost
    roi_percentage = (net_savings / monthly_token_cost * 100) if monthly_token_cost > 0 else 0

    return {
        "monthly_manual_cost_usd": round(monthly_manual_cost, 2),
        "monthly_token_cost_usd": round(monthly_token_cost, 2),
        "net_monthly_savings_usd": round(net_savings, 2),
        "roi_percentage": round(roi_percentage, 1)
    }


if __name__ == "__main__":
    metrics = calculate_monthly_roi(manual_hours=3.5, hourly_rate=45.0, daily_tokens=150000)
    print("Monthly ROI Metrics:", metrics)
