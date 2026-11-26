# Night Bite – a Mosquito-Swatting PVT

HCI Assignment 3 (Autumn 2026) – Vigilance and the Psychomotor Vigilance Test (PVT)

**Play online:** https://yu034604-crypto.github.io/HCI-Assignment3-PVT/

## Task 2 – Night Bite: Lights Off (`index.html`)

An **auditory** PVT game with a cocktail-party distractor. The room is dark and you are trying to sleep.
A mosquito flies somewhere far away while your roommate on the left is snoring. When a loud whine suddenly
starts at your **right ear**, press **SPACE** (or tap) to swat it as fast as you can. Nothing changes on screen
at stimulus onset – the task relies on hearing only.

| Reaction time | Outcome | PVT category |
|---|---|---|
| too early / < 100 ms | slapped your own ear | false start |
| 100–299 ms | squashed | valid |
| 300–499 ms | maimed (flies away with one wing) | valid |
| ≥ 500 ms | already bitten | lapse |

**PVT mechanics kept from the standard brief PVT**

- One stimulus (the near-ear whine: fixed ear, pitch and loudness, 5 ms onset ramp) and one response key → simple RT
- Random inter-stimulus interval, uniform 1–3 s; 1 s feedback; response window up to 30 s
- RT is measured from when the whine leaves the speakers (Web Audio onset mapped to `performance.now()` with `getOutputTimestamp()`) to the key event
- False starts (input before the whine is heard, or RT < 100 ms) are logged; lapses (RT ≥ 500 ms) are still timed
- 3-minute session, followed by the 7 PVT metrics from Lecture 6
  (1/RT, 1/RT500, 1/RT variability, False RT, Lapses, Fastest 10%, Slowest 10%), an RT chart and CSV export

**Snoring roommate (cocktail-party effect)**

- Every snore is synthesised anew: duration, pitch and pitch contour, loudness, roughness and resonance are randomised,
  with irregular breathing gaps, occasional pauses, double snores and snorts, and a slow loudness drift
- Snore timing is independent of the mosquito ISI, so it cannot cue the stimulus
- The snore is broadband (low throat rumble plus high turbulent hiss up to ~5 kHz) and **louder than the mosquito**:
  in offline renders the median snore peak is ~6.6 dB above the whine. The player must filter out the noise and
  focus on the target sound (cocktail-party effect). A start-screen slider adjusts the level by −12 to +6 dB (logged in the CSV)
- Narrow notches at the whine's harmonics (k × 760 Hz) keep the whine 13–22 dB above even the loudest snore at its own
  frequencies, so it is always audible: slower RTs reflect distraction, not inaudibility
- Each trial records whether the roommate was snoring at mosquito onset; the summary compares RTs for snoring vs quiet onsets
- Can be switched off on the start screen (or with `?snore=0`) for a quiet-room comparison

**How to run:** open `index.html` in Chrome (no installation needed). Use the computer's built-in keyboard and
wired headphones or built-in speakers – Bluetooth keyboards and speakers add latency the browser cannot measure
(in pilot tests, Bluetooth audio added ~120 ms and a Bluetooth keyboard ~75 ms to RTs).
For a short test, append `?dur=30` to the URL to run a 30-second session.

## Task 1 – PVT-B analysis (`pvtb_analysis.py`)

Computes the trial statistics and the 7 PVT metrics from a PsyToolkit `pvtb` raw data file.

```
pip install numpy pandas
python pvtb_analysis.py pvtb.data.2026-xxxx.txt
```

Outputs the tables to the console and saves `task1_trial_counts.csv` and `task1_pvt_metrics.csv`.
