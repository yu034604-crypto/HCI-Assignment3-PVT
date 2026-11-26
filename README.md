# Night Bite: Lights Off

HCI Assignment 3 (Autumn 2026) – Vigilance and the Psychomotor Vigilance Test (PVT)

**Play online:** https://yu034604-crypto.github.io/HCI-Assignment3-PVT/

## Task 2 – Night Bite: Lights Off (`index.html`)

Night Bite: Lights Off turns the PVT into a bedtime scene. In a dark room, players listen for a mosquito; when its loud whine suddenly appears, they press SPACE to swat it. This reduces the monotony of the PVT while keeping its core mechanics: the mosquito's sound appears after a random interval of 1–3 s, and the game records the player's reaction time in milliseconds. Each swat is graded by reaction time: pressing too early or under 100 ms slaps your own ear (false start), 100–299 ms squashes the mosquito, 300–499 ms only maims it, and 500 ms or more means it has already bitten you (lapse). Each session lasts 3 minutes and ends with the seven PVT scores.

An irregular snoring roommate is heard throughout, applying the cocktail party effect. Players must use selective attention to filter background noise and detect the mosquito. Because similar frequencies are hard to distinguish, the snoring is kept away from the whine's frequencies. The whine is therefore always audible, even through laptop speakers, and slower responses reflect distraction rather than a sound that cannot be heard.

This design replaces the visual counter with an auditory stimulus, reducing visual load. In addition, the slap sound and RT feedback appear within one perceptual processor cycle (Tp ~100 ms), so perceptual fusion makes the response feel like the cause of the kill.

**How to run:** open `index.html` in Chrome, or use the link above. Use the laptop's built-in keyboard and speakers.

## Task 1 – PVT-B analysis (`pvtb_analysis.py`)

Computes the trial statistics and the seven PVT scores from a PsyToolkit `pvtb` raw data file.

```
python pvtb_analysis.py pvtb.data.2026-xxxx.txt
```
