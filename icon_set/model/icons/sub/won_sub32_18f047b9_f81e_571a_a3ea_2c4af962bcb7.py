"""Independent 32px profile of won.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18f047b9-f81e-571a-a3ea-2c4af962bcb7', 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/won',)
SOLO_SOURCE_ICON_IDS = ('won',)
REFERENCE_EXPORT_SHA256 = 'de0fbfba3c299a969fc32ad65dc01421b6802e8876ad59f63f4e61aaf4b08c9c'

class Drawing(Sub32):
    icon_id = 'won-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 5), (24, 27))
        self.add_line('p1-r1-2', (24, 27), (16, 5))
        self.add_line('p1-r1-3', (16, 5), (8, 26))
        self.add_line('p1-r1-4', (8, 26), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (30, 15), (2, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'won-sub32': {'status': 'cannot-fix',
               'date': '2026-09-23',
               'author': 'gpt-6',
               'source_icon_id': '18f047b9-f81e-571a-a3ea-2c4af962bcb7',
               'failures_at_review': ['canvas/keyshape bounds: visible ink (0, 3, 32, 29) does not '
                                      'match the HRECT_XL envelope (0, 2, 32, 30) (deltas [0.0, '
                                      '1.0, 0.0, 1.0], tolerance 0.0)',
                                      'holes/pinches: 3 undersized holes; 0 pinches'],
               'blocker': 'The W and full middle bar create undersized enclosed openings and '
                          'pinches at 4px stroke',
               'attempts': ['Original 32px W and middle bar: three undersized holes, plus keyshape '
                            'off by 1px',
                            'Resized 32px W with lower bar: two undersized holes and two pinches'],
               'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
