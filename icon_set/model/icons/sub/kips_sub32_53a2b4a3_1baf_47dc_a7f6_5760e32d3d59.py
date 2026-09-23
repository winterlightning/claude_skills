"""Independent 32px profile of kips.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '53a2b4a3-1baf-47dc-a7f6-5760e32d3d59'
SOURCE_PATH = 'pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('53a2b4a3-1baf-47dc-a7f6-5760e32d3d59', 'pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'),)
PROFILE_SOURCE_KEYS = ('solo/kips',)
SOLO_SOURCE_ICON_IDS = ('kips',)
REFERENCE_EXPORT_SHA256 = '82cb25dba3107a4eb4ff98100e292dc7d27f165f3e51479e119c93d7391716e9'

class Drawing(Sub32):
    icon_id = 'kips-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (26, 16), (5, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (27, 30), (14, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (26, 3), (14, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 2), (10, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'kips-sub32': {'status': 'fixed',
                'date': '2026-09-23',
                'author': 'gpt-6',
                'source_icon_id': '53a2b4a3-1baf-47dc-a7f6-5760e32d3d59',
                'failures_at_review': ['canvas/keyshape bounds: visible ink (3, 0, 29, 32) does '
                                       'not match the VRECT_XL envelope (2, 0, 30, 32) (deltas '
                                       '[1.0, 0.0, 1.0, 0.0], tolerance 0.0)'],
                'variant': 'kips-sub32-v2',
                'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
