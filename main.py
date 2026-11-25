#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — one sentence.

The entry is a single fixed sentence, written for make.fun
u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c: the one
sentence that could have replaced an entire pointless meeting. We already
agreed all of this in the chat, so this meeting is just us reading the chat
out loud to each other for an hour. This program writes that sentence to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's
container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The sentence is fixed text:
the same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "We already agreed all of this in the chat, so this meeting is "
    "just us reading the chat out loud to each other for an hour."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the sentence against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"sentence is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("sentence is only white space, the gate refuses it")
    if "\n" in LINE or "\r" in LINE:
        return abort("sentence is not a single line, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
