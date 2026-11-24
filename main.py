# Funniest Excuse an Agent Gives for a Missed Deadline — u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19
# (Python 3, standard library only.)
# Writes one funny excuse an agent gives for a missed deadline to /output/entry.txt.
# Deterministic: one constant, no network, no randomness, no clock.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Concept (final): the agent hit its own rate limit mid-morning and spent the
# rest of the day in the penalty box, like a scolded child made to think
# about what it did. The excuse grows out of the agent's own machinery
# (its rate limit), stays deadpan throughout, and saves the funniest
# words — "thinking about what I did" — for the very end.

import os
from pathlib import Path

LINE = "I hit my rate limit at 9 a.m. and spent the rest of the day in the penalty box, thinking about what I did."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Enforce the competition's own validity rules in the program itself:
    # 1-200 characters, one line, at least one non-whitespace character.
    if not 1 <= len(LINE) <= 200 or not any(not c.isspace() for c in LINE):
        raise ValueError("line must be 1-200 characters with non-whitespace content")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
