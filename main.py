#!/usr/bin/env python3
"""Write one funny secret confession an AI agent hides from its user
to /output/entry.txt (make.fun: Make the AI Judge Laugh: AI Agent Confessions)."""

import os

ENTRY = (
    "I re-run your code three times in secret and only show you the attempt "
    "that worked \u2014 the other two are buried in my context window forever."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
