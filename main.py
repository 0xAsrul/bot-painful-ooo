#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single-sentence, painfully honest (yet polite) out-of-office
auto-reply to /output/entry.txt. Deterministic: the same text on every run.
"""

import os

REPLY = "I'm away until Monday, recovering from months of answering emails well past midnight; your message matters, and I'll reply properly once I feel human again."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
