"""Independent 32px profile of circle-yuan.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7b4acd01-51fe-4645-a2d7-08e28c65ee64'
SOURCE_PATH = 'pictographic-primitives/state/circle yuan_7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b4acd01-51fe-4645-a2d7-08e28c65ee64', 'pictographic-primitives/state/circle yuan_7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-yuan',)
SOLO_SOURCE_ICON_IDS = ('circle-yuan',)
REFERENCE_EXPORT_SHA256 = '6f730681cf4a400fb4e2cfe7243963dc2f6918907414e6e77477dacef8dd11b6'

class Drawing(Sub32):
    icon_id = 'circle-yuan-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 9), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 17))
        self.add_line('p2-r1-2', (16, 17), (20, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 16), (20, 9))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 17), (16, 17))
        self.add_line('p4-r1-2', (16, 17), (16, 23))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p5-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-2')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-2')
