"""Monthly subscription planning model. No dependencies, credentials, or live data."""
import argparse
import json
import math


def number(data, key, low=0, high=None, inclusive=True):
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{key} must be a finite number; unknown inputs cannot be zero-filled")
    if value < low or (not inclusive and value == low) or (high is not None and value > high):
        raise ValueError(f"{key} outside permitted range")
    return value


def evaluate(data):
    if data.get("billing") != "monthly":
        raise ValueError("Only monthly subscriptions supported; annual/weekly plans need separate cohorts")
    price = number(data, "monthly_price", inclusive=False)
    fee = number(data, "store_fee", high=1)
    refund = number(data, "refund_rate", high=1)
    variable = number(data, "variable_cost_per_payer")
    churn = number(data, "monthly_payer_churn", high=1)
    cpi = number(data, "cpi")
    conversion = number(data, "install_to_paid", high=1, inclusive=False)
    target = number(data, "target_mrr", inclusive=False)
    months = number(data, "horizon_months", low=1, high=120)
    launch = number(data, "launch_month", low=1, high=months)
    fixed = number(data, "monthly_fixed_cost")
    build = number(data, "upfront_build_cost")
    if int(months) != months or int(launch) != launch:
        raise ValueError("Month inputs must be integers")
    months, launch = int(months), int(launch)
    net = price * (1-refund) * (1-fee)
    unit = net-variable
    cac = cpi/conversion
    target_payers = math.ceil(target/price)
    active_months = months-launch+1
    factor = sum((1-churn)**k for k in range(active_months))
    new_payers = math.ceil(target_payers/factor)
    payers = 0
    cumulative = -build
    funding_gap = build
    rows = []
    for month in range(1, months+1):
        acquired = new_payers if month >= launch else 0
        payers = payers*(1-churn)+acquired
        spend = acquired*cac
        contribution = payers*unit
        operating = contribution-spend-fixed
        cumulative += operating
        funding_gap = max(funding_gap, -cumulative)
        rows.append({"month": month, "active_payers": payers, "new_payers": acquired,
                     "installs": acquired/conversion, "gross_mrr": payers*price,
                     "net_proceeds": payers*net, "acquisition_spend": spend,
                     "contribution_before_acquisition": contribution,
                     "after_acquisition_and_fixed": operating, "cumulative_cash": cumulative})
    ltv = unit/churn if churn > 0 and unit > 0 else None
    ratio = ltv/cac if ltv is not None and cac > 0 else None
    payback = cac/unit if unit > 0 else None
    budget = data.get("monthly_acquisition_budget")
    if budget is not None:
        number(data, "monthly_acquisition_budget")
    risk = data.get("total_risk_budget")
    if risk is not None:
        number(data, "total_risk_budget")
    capital = "UNRESOLVED" if budget is None or risk is None else (
        "WITHIN_MODELED_BUDGET" if new_payers*cac <= budget and funding_gap <= risk else "EXCEEDS_MODELED_BUDGET")
    return {"model": "hypothetical constant monthly cohorts; end-of-month arrivals; no organic acquisition",
            "unit_contribution": unit, "paid_cac": cac, "contribution_ltv_approx": ltv,
            "ltv_cac": ratio, "payback_months": payback,
            "base_economics_gate": unit > 0 and ratio is not None and ratio >= 3 and payback <= 3,
            "target_payers": target_payers, "maintenance_new_payers_monthly": target_payers*churn,
            "constant_new_payers_per_selling_month": new_payers,
            "required_monthly_acquisition_spend": new_payers*cac,
            "peak_cumulative_funding_gap": funding_gap, "capital_feasibility": capital,
            "months": rows,
            "limitations": ["No fee remittance delays, taxes, or financing costs",
                            "Fractional expected survivors; constant CAC and churn; channel capacity unproven",
                            "MRR and cash approximations do not validate demand or retention",
                            "Zero churn or zero paid CAC leaves LTV/CAC undefined, never an automatic pass"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Scenario JSON, not an AppKittie response")
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8") as handle:
            result = evaluate(json.load(handle))
        print(json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, OSError) as error:
        parser.exit(2, f"Invalid scenario: {error}\n")
