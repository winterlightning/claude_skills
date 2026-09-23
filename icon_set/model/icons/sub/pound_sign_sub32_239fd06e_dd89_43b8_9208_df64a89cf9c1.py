"""Independent 32px profile of pound-sign.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '239fd06e-dd89-43b8-9208-df64a89cf9c1'
SOURCE_PATH = 'pictographic-primitives/symbol/pound_239fd06e-dd89-43b8-9208-df64a89cf9c1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('239fd06e-dd89-43b8-9208-df64a89cf9c1', 'pictographic-primitives/symbol/pound_239fd06e-dd89-43b8-9208-df64a89cf9c1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pound-sign',)
SOLO_SOURCE_ICON_IDS = ('pound-sign',)
REFERENCE_EXPORT_SHA256 = '618b20769523037d57430d31503fd9951221548ca489e2bcb99381934047246d'

class Drawing(Sub32):
    icon_id = 'pound-sign-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (27, 10), ((27, 6), (23, 2), (19, 2)))
        self.add_bezier('p1-r1-2', (19, 2), ((14, 2), (10, 6), (10, 10)))
        self.add_line('p1-r1-3', (10, 10), (10, 17))
        self.add_line('p1-r1-4', (10, 17), (10, 23))
        self.add_arc('p1-r1-5', (10, 23), (5, 30), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 17), (10, 17))
        self.add_line('p2-r1-2', (10, 17), (20, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (5, 30), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'pound-sign-sub32': {'status': 'fixed',
                      'date': '2026-09-23',
                      'author': 'gpt-6',
                      'source_icon_id': '239fd06e-dd89-43b8-9208-df64a89cf9c1',
                      'failures_at_review': ['canvas/keyshape bounds: visible ink (3, 0, 29, 32) '
                                             'does not match the VRECT_XL envelope (2, 0, 30, 32) '
                                             '(deltas [1.0, 0.0, 1.0, 0.0], tolerance 0.0)'],
                      'variant': 'pound-sign-sub32-v2',
                      'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
