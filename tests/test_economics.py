import copy
import json
import unittest
from pathlib import Path
from scripts.economics import evaluate


class EconomicsTests(unittest.TestCase):
    def setUp(self):
        self.scenario = json.loads((Path(__file__).resolve().parents[1]/"examples/economics.json").read_text())

    def test_reference_monthly_arithmetic_and_target(self):
        r = evaluate(self.scenario)
        self.assertAlmostEqual(r["unit_contribution"], 11.359255)
        self.assertAlmostEqual(r["paid_cac"], 116.6666666667)
        self.assertEqual(r["target_payers"], 2669)
        self.assertFalse(r["base_economics_gate"])
        self.assertEqual(r["months"][0]["new_payers"], 0)
        self.assertGreaterEqual(r["months"][-1]["gross_mrr"], 40000)
        self.assertEqual(r["capital_feasibility"], "UNRESOLVED")

    def test_launch_delay_increases_acquisition_requirement(self):
        early = evaluate(self.scenario)
        self.scenario["launch_month"] = 4
        late = evaluate(self.scenario)
        self.assertGreater(late["required_monthly_acquisition_spend"], early["required_monthly_acquisition_spend"])

    def test_good_ratio_does_not_override_bad_payback(self):
        self.scenario.update(monthly_payer_churn=0.02, cpi=1.5)
        r = evaluate(self.scenario)
        self.assertGreater(r["ltv_cac"], 3)
        self.assertGreater(r["payback_months"], 3)
        self.assertFalse(r["base_economics_gate"])

    def test_unprofitable_units_cannot_pass(self):
        self.scenario["variable_cost_per_payer"] = 25
        r = evaluate(self.scenario)
        self.assertLess(r["unit_contribution"], 0)
        self.assertIsNone(r["payback_months"])
        self.assertFalse(r["base_economics_gate"])

    def test_cash_budget_and_fixed_build_costs(self):
        self.scenario.update(monthly_acquisition_budget=1, total_risk_budget=1,
                             upfront_build_cost=1000, monthly_fixed_cost=500)
        r = evaluate(self.scenario)
        self.assertEqual(r["capital_feasibility"], "EXCEEDS_MODELED_BUDGET")
        self.assertEqual(r["months"][0]["cumulative_cash"], -1500)

    def test_unknown_invalid_and_unsupported_inputs(self):
        cases = [{"monthly_price": None}, {"cpi": float("nan")}, {"install_to_paid": 0},
                 {"monthly_payer_churn": 1.1}, {"horizon_months": 1.5},
                 {"launch_month": 7}, {"billing": "annual"}, {"store_fee": True}]
        for patch in cases:
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                evaluate(dict(self.scenario, **patch))

    def test_zero_churn_and_zero_cac_are_not_infinite_ltv(self):
        for patch in ({"monthly_payer_churn": 0}, {"cpi": 0}):
            r = evaluate(dict(self.scenario, **patch))
            self.assertIsNone(r["ltv_cac"])
            self.assertFalse(r["base_economics_gate"])


if __name__ == "__main__":
    unittest.main()
