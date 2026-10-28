"""Where the fill side-pair engine reads and writes.

DATA is tracked source data (icon_set/data/side-fill): the imported layouts, picks, review decisions,
the source drawings each fill was made from, the fills and the region recipes. A build never writes it.
WORK is ignored build output (icon_set/state/side-fill): recombined renders, layout renders, reports.
The published pages come from `python3 -m icon_set side-fill publish`, not from WORK directly.
"""
from pathlib import Path

ICON_SET = Path(__file__).resolve().parents[2]
DATA = ICON_SET / 'data' / 'side-fill'
WORK = ICON_SET / 'state' / 'side-fill'
FILL_ENGINE = ICON_SET / 'vendor' / 'fill_processing' / 'vendor'
