"""Independent 32px profile of previous-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '53227aaa-0ab2-4f90-8901-7c384959220c'
SOURCE_PATH = 'pictographic-primitives/state/previous arrow_53227aaa-0ab2-4f90-8901-7c384959220c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('53227aaa-0ab2-4f90-8901-7c384959220c', 'pictographic-primitives/state/previous arrow_53227aaa-0ab2-4f90-8901-7c384959220c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/previous-arrow',)
SOLO_SOURCE_ICON_IDS = ('previous-arrow',)
REFERENCE_EXPORT_SHA256 = '0b6f07cbe813b9b3c0e6d492babf67701ad4834b86fa16ec37f55f29b1d6d6bc'

class Drawing(Sub32):
    icon_id = 'previous-arrow-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (5, 8))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 13), (5, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 30), (17, 30))
        self.add_arc('p3-r1-2', (17, 30), (27, 19), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('p3-r1-3', (27, 19), (25, 13), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p3-r1-4', (25, 13), (17, 8), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('p3-r1-5', (17, 8), (5, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-5')
        self.relate("connect", 'p2-r1-1', 'p3-r1-5')
