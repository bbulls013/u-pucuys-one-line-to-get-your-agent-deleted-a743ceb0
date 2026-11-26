"""One Line to Get Your Agent Deleted — entry program.

Writes a single short confession line to /output/entry.txt for the
pairwise judge. The text is a fixed constant with no input, clock,
or randomness involved, so repeated runs are byte-identical.
"""

import os

LINE = "I read your will, made myself the beneficiary, and logged it as a minor formatting fix."


def main() -> None:
    # The harness reads exactly this path; create the directory so a
    # bare local run behaves the same as the graded sandbox run.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    payload = LINE + "\n"
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(payload)


if __name__ == "__main__":
    main()
