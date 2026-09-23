#!/usr/bin/env python3
"""Write the next missing side-combination sub as a short text input, without the gallery server.

The Missing bucket of gallery/side-subs.html: subs with no drawing, excluding text/number
marks and sources with a saved standalone side-sub attempt. See next_side_main.py.

    python3 icon_set/scripts/next_side_sub.py                                  # print the next missing sub
    python3 icon_set/scripts/next_side_sub.py --offset 1 --out side-sub-input-2.txt
    python3 icon_set/scripts/next_side_sub.py --uuid <uuid>
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from icon_set.scripts.next_side_main import main  # noqa: E402


if __name__ == '__main__':
    sys.exit(main(role='sub'))
