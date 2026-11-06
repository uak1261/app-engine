"""Monthly revenue/download trends from saved get_app_historicals responses.
Usage: python3 -I scripts/revenue_trends.py research/<date>/raw > out.json
Monthly value = mean of daily snapshots of AppKittie's estimated monthly revenue within that calendar month.
"""
import json, glob, os, sys, datetime as dt, statistics as st
raw = sys.argv[1]
res = []
for f in sorted(glob.glob(os.path.join(raw, "hist_*.json"))):
    d = json.load(open(f))["data"]; hc = d["historical_counts"]
    def monthly(key):
        m = {}
        for p in hc.get(key, []):
            k = dt.datetime.fromtimestamp(p["date_created_timestamp"], dt.timezone.utc).strftime("%Y-%m")
            m.setdefault(k, []).append(p["value"] or 0)
        return {k: st.mean(v) for k, v in sorted(m.items())}
    rev, dl = monthly("revenue"), monthly("downloads")
    months = list(rev)
    first30 = next((k for k in months if rev[k] >= 30000), None)
    last3 = [rev[k] for k in months[-3:]]
    res.append({"file": os.path.basename(f), "title": d["title"], "tracked_from": months[0] if months else None,
        "months": len(months), "first_month_ge_30k": first30, "peak_k": round(max(rev.values())/1000) if rev else None,
        "peak_month": max(rev, key=rev.get) if rev else None, "latest_k": round(rev[months[-1]]/1000) if rev else None,
        "three_month_change_pct": round(100*(last3[-1]/last3[0]-1)) if len(last3)==3 and last3[0] else None,
        "monthly_rev_k": {k: round(v/1000) for k, v in rev.items()},
        "monthly_dl_k": {k: round(v/1000,1) for k, v in dl.items()}})
print(json.dumps(res, indent=1))
