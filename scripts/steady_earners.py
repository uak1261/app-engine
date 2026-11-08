"""Rank apps by steady estimated revenue over a 3-month window, with observed review velocity.
Usage: python3 -I scripts/steady_earners.py <months comma list, e.g. 2026-08,2026-09,2026-10> <hist files...>
Revenue = mean of AppKittie daily 'estimated monthly revenue' snapshots per month (vendor-estimated).
Reviews = App Store review count (observed by AppKittie's scraper), change across the window.
"""
import json, sys, datetime as dt, statistics as st
months = sys.argv[1].split(","); out = []
for f in sys.argv[2:]:
    d = json.load(open(f))["data"]; hc = d["historical_counts"]
    def bymonth(key, agg):
        m = {}
        for p in hc.get(key, []):
            k = dt.datetime.fromtimestamp(p["date_created_timestamp"], dt.timezone.utc).strftime("%Y-%m")
            if p["value"] is not None: m.setdefault(k, []).append(p["value"])
        return {k: agg(v) for k, v in m.items()}
    rev = bymonth("revenue", st.mean); rv_first = bymonth("reviews", lambda v: v[0]); rv_last = bymonth("reviews", lambda v: v[-1])
    if not all(m in rev for m in months): continue
    vals = [rev[m] for m in months]
    r0, r1 = rv_first.get(months[0]), rv_last.get(months[-1])
    out.append({"file": f.split("/")[-1], "slug": d["app_slug"], "title": d["title"], "rev_by_month_k": [round(v/1000,1) for v in vals],
        "avg_k": round(st.mean(vals)/1000,1), "min_k": round(min(vals)/1000,1), "max_over_min": round(max(vals)/min(vals),2) if min(vals) else None,
        "cv": round(st.pstdev(vals)/st.mean(vals),3) if st.mean(vals) else None,
        "reviews_start": r0, "reviews_end": r1, "new_reviews_window": (r1-r0) if r0 is not None and r1 is not None else None})
print(json.dumps(out, indent=1))
