from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "gcp/output"
OUT.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(ROOT / "shared/data/mobility_trips.csv")
df["event_id"] = df.event_id.astype("string").str.strip()
df["trip_id"] = df.trip_id.astype("string").str.strip()
df["event_timestamp"] = pd.to_datetime(df.event_timestamp, errors="coerce", utc=True)
df["duration_minutes"] = pd.to_numeric(df.duration_minutes, errors="coerce")
df["distance_km"] = pd.to_numeric(df.distance_km, errors="coerce")
df = df.sort_values("event_timestamp").drop_duplicates("event_id", keep="last")
valid = (df.event_id.notna() & df.trip_id.notna() & df.event_timestamp.notna()
         & (df.duration_minutes > 0) & (df.distance_km >= 0) & df.service_area.notna())
good, bad = df[valid].copy(), df[~valid].copy()
good["event_date"] = good.event_timestamp.dt.date.astype(str)
good.to_csv(OUT / "mobility_curated.csv", index=False)
bad.to_csv(OUT / "mobility_quarantine.csv", index=False)
(good.groupby(["event_date","service_area"])
 .agg(trip_count=("trip_id","nunique"), avg_duration=("duration_minutes","mean"),
      total_distance_km=("distance_km","sum"))
 .reset_index()).to_csv(OUT / "daily_metrics.csv", index=False)
print(f"Curated={len(good)}; quarantined={len(bad)}")
