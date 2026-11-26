"""
HCI Assignment 3 - Task 1.2: PVT-B data analysis
Usage:  python pvtb_analysis.py pvtb.data.2026-xxxx.txt

PsyToolkit pvtb raw-data columns (one row per trial, space separated):
  c1  trial number
  c2  status: 1 = valid response, 2 = false start (too early), 3 = lapse (RT >= 500 ms)
  c3  inter-stimulus interval / random wait before stimulus (ms)
  c4  time since experiment start (ms)
  c5  internal timing value (not used)
  c6  reaction time RT (ms); 0 for false starts
  c7  running mean RT of valid trials (computed by PsyToolkit)
  c8  trial counter
  c9  cumulative number of lapses
  c10 cumulative number of false starts
"""
import sys
import numpy as np
import pandas as pd

MIN_RT = 100     # RT < 100 ms  -> false start / anticipation
LAPSE_RT = 500   # RT >= 500 ms -> lapse (as defined in the assignment)

cols = ["trial", "status", "isi", "t_since_start", "internal",
        "rt", "running_mean", "trial_count", "cum_lapses", "cum_false_starts"]

path = sys.argv[1] if len(sys.argv) > 1 else "pvtb.data.txt"
df = pd.read_csv(path, sep=r"\s+", header=None, names=cols)

# --- classify trials (status code AND RT thresholds) ---
false_start = (df["status"] == 2) | (df["rt"] < MIN_RT)
lapse = ~false_start & ((df["status"] == 3) | (df["rt"] >= LAPSE_RT))
valid = ~false_start & ~lapse                 # 100 <= RT < 500 ms
responses = df.loc[~false_start, "rt"]        # all RTs >= 100 ms (valid + lapses)

n_total = len(df)
n_fs, n_lapse, n_valid = int(false_start.sum()), int(lapse.sum()), int(valid.sum())

# Mean and median RT (ms) are also printed for reference.
# --- 7 standard PVT metrics (HCI Lecture Topic 06, slides "PVT Scores") ---
# All reciprocal measures are in 1/seconds: 1/RT = 1000 / RT(ms).
rt = np.sort(responses.to_numpy(dtype=float))  # all responses with RT >= 100 ms
recip = 1000.0 / rt                            # sorted descending speed (fastest first)
k = max(1, int(round(0.10 * len(rt))))         # 10 % of responses
rt500 = rt[rt <= LAPSE_RT]                     # lapses excluded

metrics = {
    "1. 1/RT: mean reciprocal RT, all responses (1/s)":      recip.mean(),
    "2. 1/RT500: mean reciprocal RT, lapses excluded (1/s)": (1000.0 / rt500).mean(),
    "3. 1/RT variability: P90 - P10 of 1/RT (1/s)":
        np.percentile(recip, 90) - np.percentile(recip, 10),
    "4. False RT: false starts / valid stimuli (%)":         100.0 * n_fs / len(rt),
    "5. Lapses: number (RT >= 500 ms)":                      n_lapse,
    "   Lapses: proportion of responses (%)":                100.0 * n_lapse / len(rt),
    "6. Fastest 10%: mean 1/RT of fastest 10% (1/s)":        recip[:k].mean(),
    "7. Slowest 10%: mean 1/RT of slowest 10% (1/s)":        recip[-k:].mean(),
}

counts = pd.DataFrame({
    "Item": ["Total trials", "Valid trials (100 <= RT < 500 ms)",
             "Error trials (total)", "  - False starts (RT < 100 ms)",
             "  - Lapses (RT >= 500 ms)"],
    "Value": [n_total, n_valid, n_fs + n_lapse, n_fs, n_lapse],
})
perf = pd.DataFrame({"Metric": list(metrics),
                     "Value": [f"{v:.2f}" if isinstance(v, float) else str(v)
                               for v in metrics.values()]})

print("=== Basic trial statistics ===")
print(counts.to_string(index=False))
print(f"\n=== Performance summary (n = {len(rt)} responses with RT >= {MIN_RT} ms) ===")
print(perf.to_string(index=False))
print(f"\nReference: mean RT = {rt.mean():.2f} ms, median RT = {np.median(rt):.2f} ms")
print(f"(Mean RT of valid trials only = {df.loc[valid, 'rt'].mean():.2f} ms; "
      f"PsyToolkit summary shows {df['running_mean'].iloc[-1]:.0f} ms)")

counts.to_csv("task1_trial_counts.csv", index=False)
perf.to_csv("task1_pvt_metrics.csv", index=False)
print("\nSaved: task1_trial_counts.csv, task1_pvt_metrics.csv")
