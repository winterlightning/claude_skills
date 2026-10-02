"""Goldens for combine-side.js `transfer`: combination_layouts.transfer on hand-made layouts.

    python3 icon_set/tests/js/make_transfer_goldens.py   # writes icon_set/tests/js/transfer-goldens.json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.combination_layouts import transfer  # noqa: E402

LAYOUT = {'main': [{'paths': [0], 'x': 4, 'y': 6, 'w': 30, 'h': 28}, {'paths': [1, 2], 'x': 12, 'y': 36, 'w': 0, 'h': 9}],
          'sub': [{'paths': [0, 1], 'x': 41, 'y': 40, 'w': 19, 'h': 18}, {'paths': [2], 'x': 50, 'y': 44, 'w': 7, 'h': 0}]}
TARGET_SUB = [{'paths': [0], 'box': [38, 38, 58, 57]}, {'paths': [1, 2], 'box': [44, 41.5, 59.25, 60]}]
cases = []
for position in ('br', 'bl', 'tr', 'tl', 'ri', 'le', 'bo', 'to'):
    for same_sub in (True, False):
        for canvas in (64, 72):
            args = dict(layout=LAYOUT, source_position='br', source_sub='sub/a', target_position=position,
                        target_sub='sub/a' if same_sub else 'sub/b', target_canvas=canvas,
                        target_sub_groups=None if same_sub else TARGET_SUB)
            cases.append({'args': args, 'out': transfer(**args)})
cases.append({'args': dict(layout={'main': LAYOUT['main']}, source_position='tr', source_sub='sub/a', target_position='le',
                           target_sub='sub/b', target_canvas=64, target_sub_groups=None),
              'out': transfer({'main': LAYOUT['main']}, 'tr', 'sub/a', 'le', 'sub/b', 64, None)})
Path(__file__).with_name('transfer-goldens.json').write_text(json.dumps(cases, indent=1) + '\n')
print(len(cases), 'cases')
