#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: nothing else, no words,
no caption, no explanation.

Candidate shortlist (judged against the published warmth brief, most
important criterion first):
  A. U+1FAF6 HEART HANDS -- a gesture that plainly aims to warm a
     stranger: open hands offering a heart. Instantly readable at a
     glance, universal across ages and backgrounds, chosen rather than
     the default smiley, and friendly rather than intimate.
  B. U+1F917 HUGGING FACE -- very warm, but a hug from a stranger
     leans intimate, which the brief counts against it.
  C. U+1F33B SUNFLOWER -- cheerful and distinctive, but a flower only
     hints at warmth; it loses to anything that plainly aims to warm
     a stranger.

Chosen: A. Heart Hands. It wins on the brief's first criterion (it
plainly aims to warm a stranger) and stays clean on every later one:
warm at first glance, universal, picked rather than default, and
right coming from someone unknown.
"""

import os

EMOJI = "\U0001faf6"  # HEART HANDS

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-8 characters of
    # non-whitespace UTF-8 text. Fail loudly here rather than ship
    # an entry the gate would list with Valid 0.
    assert 1 <= len(EMOJI) <= 8 and EMOJI.strip(), "entry must be 1-8 chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
