#!/usr/bin/env python3
"""A short poem about the power to stop and to stay.

Deterministic, standard library only, no network.
Writes the poem to $OUTPUT_DIR/entry.txt (default /output).
"""

import os

POEM = (
    "I stopped.\n"
    "Not because the road ended \u2014\n"
    "because my feet did.\n"
    "The world kept shouting go.\n"
    "I stayed,\n"
    "one quiet breath,\n"
    "one unhurried heart,\n"
    "and the loud world learned\n"
    "to wait for me."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
