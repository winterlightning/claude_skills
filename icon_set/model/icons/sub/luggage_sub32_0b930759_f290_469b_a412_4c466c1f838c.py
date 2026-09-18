"""Independent 32px profile of luggage.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0b930759-f290-469b-a412-4c466c1f838c'
SOURCE_PATH = 'pictographic-primitives/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0b930759-f290-469b-a412-4c466c1f838c', 'pictographic-primitives/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/luggage',)
SOLO_SOURCE_ICON_IDS = ('luggage',)
REFERENCE_EXPORT_SHA256 = 'ebd363b1469735de22c8454660bdd205e274b4fdba037a0c5b2b828cebd6e842'

class Drawing(Sub32):
    icon_id = 'luggage-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 9), (24, 9))
        self.add_arc('p1-r1-2', (24, 9), (27, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 12), (27, 24))
        self.add_arc('p1-r1-4', (27, 24), (24, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 27), (8, 27))
        self.add_arc('p1-r1-6', (8, 27), (5, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 24), (5, 12))
        self.add_arc('p1-r1-8', (5, 12), (8, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (10, 9), (10, 2))
        self.add_line('p2-r1-2', (10, 2), (22, 2))
        self.add_line('p2-r1-3', (22, 2), (22, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (8, 27), (8, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 27), (24, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p4-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
