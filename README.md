# Night Bite – a Mosquito-Swatting PVT

HCI Assignment 3 (Autumn 2026) – Vigilance and the Psychomotor Vigilance Test (PVT)

**Play online:** https://yu034604-crypto.github.io/HCI-Assignment3-PVT/

## Task 2 – Night Bite (`index.html`)

A PVT-based game. Late at night, your hand rests under a desk lamp while a mosquito buzzes in the dark.
When the mosquito lands in the lamp light, press **SPACE** (or tap) to swat it as fast as you can.

| Reaction time | Outcome | PVT category |
|---|---|---|
| before landing / < 100 ms | slapped yourself | false start |
| 100–249 ms | squashed | valid |
| 250–499 ms | maimed (flies away with one wing) | valid |
| ≥ 500 ms | already bitten | lapse |

**PVT mechanics kept from the standard brief PVT**

- Single fixed stimulus location and fixed mosquito size; one response key (simple RT)
- Random inter-stimulus interval, uniform 1–3 s
- RT measured in ms from the frame in which the mosquito is first drawn to the input event (`performance.now()` time base)
- False starts (input during the ISI or RT < 100 ms) are logged; lapses (RT ≥ 500 ms) are still timed
- 3-minute session, followed by a summary of the 7 PVT metrics from Lecture 6
  (1/RT, 1/RT500, 1/RT variability, False RT, Lapses, Fastest 10%, Slowest 10%),
  a reaction-time chart, and CSV export of trial data and summary

**How to run:** open `index.html` in Chrome (no installation needed). Use headphones or speakers.
For a short test, append `?dur=30` to the URL to run a 30-second session.

## Task 1 – PVT-B analysis (`pvtb_analysis.py`)

Computes the trial statistics and the 7 PVT metrics from a PsyToolkit `pvtb` raw data file.

```
pip install numpy pandas
python pvtb_analysis.py pvtb.data.2026-xxxx.txt
```

Outputs the tables to the console and saves `task1_trial_counts.csv` and `task1_pvt_metrics.csv`.
