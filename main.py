"""The Robot Apology — deterministic entry writer.

Writes one fixed two-line robot confession to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic by design: no clock, no randomness, no network,
no file reads. The same input always produces the same bytes,
so two runs hash identically.
"""

import os

ENTRY = (
    "I am sorry I alphabetized your spice rack and put the cinnamon "
    "where the cumin lived, so your chili tasted like Christmas morning.\n"
    "I learned that tidy is not the same as useful, so from now on I "
    "will shelve spices by your recipes, not by the alphabet.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
