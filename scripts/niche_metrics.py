"""Compute niche-level metrics from saved AppKittie search responses.
Usage: python3 -I scripts/niche_metrics.py research/<date>/raw research/<date>/analysis/niche_map.json
Metrics use AppKittie monthly estimates (vendor-estimated). Rows are deduplicated by app_slug.
"""
import json, re, sys, os, datetime as dt
raw, mp = sys.argv[1], json.load(open(sys.argv[2]))
asof = dt.datetime(2026,11,5)
out = []
for niche, spec in mp.items():
    rows = {}
    for f in spec["files"]:
        for a in json.load(open(os.path.join(raw, f)))["data"]:
            if re.search(spec["include"], a["title"]): rows[a["app_slug"]] = a
    apps = sorted(rows.values(), key=lambda a: -a["revenue"])
    tot = sum(a["revenue"] for a in apps)
    pubs = {}
    for a in apps: pubs[a["developer"]] = pubs.get(a["developer"],0)+a["revenue"]
    rel = lambda a: dt.datetime.fromtimestamp(a["app_released_date_timestamp"], dt.timezone.utc).replace(tzinfo=None)
    recent = [a for a in apps if (asof-rel(a)).days <= 548 and a["revenue"]>=20000]
    meta = [a.get("meta_ads_estimated_spend_30d_usd") for a in apps]
    out.append({
      "niche": niche, "apps": len(apps), "publishers_ge_20k": sum(1 for v in pubs.values() if v>=20000),
      "niche_rev_est_k": round(tot/1000), "leader_share_pct": round(100*max(pubs.values())/tot) if tot else None,
      "hhi": round(sum((v/tot*100)**2 for v in pubs.values())) if tot else None,
      "entrants_le_18mo_ge_20k": len(recent),
      "median_rev_growth_30d": sorted(a["historical_counts"]["revenue_growth_30d"] for a in apps)[len(apps)//2],
      "mean_rating_top3": round(sum(a["score"] for a in apps[:3])/min(3,len(apps)),2),
      "meta_known": sum(1 for m in meta if m is not None), "meta_30d_sum_k": round(sum(m for m in meta if m)/1000),
      "non_us_storefronts": sum(1 for a in apps if "/us/" not in a["url"]),
      "top": "; ".join(f'{a["title"][:28]} ${round(a["revenue"]/1000)}K ({rel(a):%Y-%m})' for a in apps[:4])})
print(json.dumps(out, indent=1))
