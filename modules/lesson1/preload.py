cs_long_name = "Lesson 1: Prepping for the 5K"

import math, random

# # Deterministic per-student randomness
# csm_tutor.init_random()

# --- Per-user workout sample -----------------------------------------------
miles_today        = 10
minutes_today      = 20
seconds_today      = 5
total_seconds_today = minutes_today * 60 + seconds_today
expected_pace_today = (total_seconds_today / 60) / miles_today       # min/mi
# ---------------------------------------------------------------------------
