"""The Funniest Office Joke — make.fun entry.

Writes a single-line joke about office life to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The joke is one line on purpose:
setup, turn, punchline last — nothing after it.
"""

import os

ENTRY = "I replied-all to say 'please stop replying-all' and now I'm the reason there's a company-wide policy named after me."

# Gate from the competition rules: UTF-8 text, 1 to 200 characters,
# a single line, plain text, no explanation of its own joke.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
