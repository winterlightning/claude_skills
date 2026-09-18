"""Independent 32px profile of state32-229ee448-4dc8-470b-ac1f-fbbfcd586284.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '229ee448-4dc8-470b-ac1f-fbbfcd586284'
SOURCE_PATH = 'pictographic-primitives/state/needles two_229ee448-4dc8-470b-ac1f-fbbfcd586284.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('229ee448-4dc8-470b-ac1f-fbbfcd586284', 'pictographic-primitives/state/needles two_229ee448-4dc8-470b-ac1f-fbbfcd586284.svg'),)
PROFILE_SOURCE_KEYS = ('solo/needles-two',)
SOLO_SOURCE_ICON_IDS = ('needles-two',)
REFERENCE_EXPORT_SHA256 = 'd7e736475021d90c7a08f4300c715f916cdc99d07032fb12ba47cfae866ab62c'

class Drawing(Sub32):
    icon_id = 'state32-229ee448-4dc8-470b-ac1f-fbbfcd586284'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 10), (2, 20))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 26), (22, 26))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (10, 6), (18, 6), radius_x=4, radius_y=4, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (18, 6), (10, 6), radius_x=4, radius_y=4, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (22, 26), (30, 26), radius_x=4, radius_y=4, large_arc=True, sweep=False)
        self.add_arc('p4-r1-2', (30, 26), (22, 26), radius_x=4, radius_y=4, large_arc=True, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-2')
