"""Funniest Time Machine Warning Label.

Writes one warning label to /output/entry.txt: a straight-faced safety
notice whose punchline is a paradox — the label itself is the reason
the traveller is in danger.
"""

import os

LABEL = "WARNING: Never step out before 1900. Your great-grandfather is armed — and he has already read this label."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
