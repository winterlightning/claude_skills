"""Independent 32px profile of mechanical-robotic-hand-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6444a5ca-ed45-4973-a423-c42fca7fd778'
SOURCE_PATH = 'pictographic-primitives/other/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6444a5ca-ed45-4973-a423-c42fca7fd778', 'pictographic-primitives/other/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mechanical-robotic-hand-solo',)
SOLO_SOURCE_ICON_IDS = ('mechanical-robotic-hand-solo',)
REFERENCE_EXPORT_SHA256 = 'b8926cc2cf3a0de9e433d7b62ad8b65f0c65d40fb47b37f680e3d8ee52251f92'

class Drawing(Sub32):
    icon_id = 'mechanical-robotic-hand-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 5), ((8, 5), (12, 8), (16, 9)))
        self.add_arc('p1-r1-2', (16, 9), (19, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (19, 12), (19, 16))
        self.add_line('p1-r1-4', (19, 16), (25, 10))
        self.add_bezier('p1-r1-5', (25, 10), ((26, 9), (27, 9), (28, 9)))
        self.add_bezier('p1-r1-6', (28, 9), ((29, 9), (30, 10), (30, 12)))
        self.add_bezier('p1-r1-7', (30, 12), ((30, 15), (24, 21), (22, 24)))
        self.add_bezier('p1-r1-8', (22, 24), ((18, 27), (15, 27), (13, 27)))
        self.add_bezier('p1-r1-9', (13, 27), ((8, 27), (6, 24), (2, 23)))
        self.add_line('p1-r1-10', (2, 23), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (8, 8), (8, 25))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
