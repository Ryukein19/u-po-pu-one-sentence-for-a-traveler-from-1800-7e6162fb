import os
# One-liner entry: the line below is the whole submission.
LINE = "Imagine a web of copper threads joining every house, so a letter from London reaches Boston before the ink is dry, and any man may ask a question and hear a thousand voices answer."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
