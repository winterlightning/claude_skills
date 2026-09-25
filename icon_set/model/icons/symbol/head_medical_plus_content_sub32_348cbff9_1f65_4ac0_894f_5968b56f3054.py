"""Independent 32px profile of head-medical-plus-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '348cbff9-1f65-4ac0-894f-5968b56f3054'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/348cbff9-1f65-4ac0-894f-5968b56f3054.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('348cbff9-1f65-4ac0-894f-5968b56f3054', 'icon_set/dist/gallery/combination-originals/348cbff9-1f65-4ac0-894f-5968b56f3054.svg'),)
PROFILE_SOURCE_KEYS = ('solo/head-medical-plus-content',)
SOLO_SOURCE_ICON_IDS = ('head-medical-plus-content',)
REFERENCE_EXPORT_SHA256 = 'bca06590ffc5c7f7e6b5fbc7fbf2acab5e8565153a8aefc84922c41541f692af'

class Drawing(Sub32):
    icon_id = 'head-medical-plus-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 30), (8, 23))
        self.add_arc('p1-r1-2', (8, 23), (5, 16), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (5, 16), (5, 12))
        self.add_arc('p1-r1-4', (5, 12), (15, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (15, 2), (24, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (24, 12), (27, 17))
        self.add_line('p1-r1-7', (27, 17), (23, 19))
        self.add_line('p1-r1-8', (23, 19), (23, 24))
        self.add_line('p1-r1-9', (23, 24), (19, 24))
        self.add_line('p1-r1-10', (19, 24), (19, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (15, 13), (11, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (15, 13), (18, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (15, 13), (15, 10))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (15, 13), (15, 17))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
