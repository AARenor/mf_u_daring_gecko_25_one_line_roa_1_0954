#!/usr/bin/env python3
"""Write one short roast line for a make.fun bounty.

Standard library only, no network. The text is a single constant below and is
written as UTF-8 bytes with no trailing newline into MAKEFUN_OUTPUT_DIR when
that variable is set, otherwise into /output.
"""

import os
import sys

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
