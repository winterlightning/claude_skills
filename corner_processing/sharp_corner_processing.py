#!/usr/bin/env python3
"""sharp_corner_processing.py — build the all-sharp version of the 48x48 icon set.

Detects the corners of the input icons, builds the all-sharp output and checks it, then
rebuilds the review pages. The steps live in core/pipeline.py; the rules in core/toggle.py.

  python3 sharp_corner_processing.py                          # the whole set
  python3 sharp_corner_processing.py --files add-tab.svg       # chosen icons (others kept)
  python3 sharp_corner_processing.py --sample 100 --no-report
  python3 sharp_corner_processing.py --help
"""

import sys

from core.pipeline import run

if __name__ == "__main__":
    sys.exit(run("sharp"))
