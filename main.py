#!/usr/bin/env python3
"""One word for my Wi-Fi: Friendzoned.

The router lets me in, shows full bars, remembers my name — and then
loads absolutely nothing. We are connected. We are not together. It
keeps me around for the company and gives me nothing back, which is
exactly what being friendzoned is, except the friend is a small box
with blinking lights that I have to unplug and plug back in before it
will even look at me.
"""

import os
import sys

WORD = "Friendzoned"


def main():
    word = WORD
    if not word:
        raise SystemExit("no word to write")
    if len(word) > 20:
        raise SystemExit("word is %d chars, gate allows at most 20" % len(word))
    for ch in word:
        if ch.isspace():
            raise SystemExit("word must be a single word with no whitespace")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    data = word.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        again = handle.read()
    if again != data:
        raise SystemExit("entry.txt on disk differs from the word")
    print("entry.txt <- %s (%d chars)" % (path, len(word)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
