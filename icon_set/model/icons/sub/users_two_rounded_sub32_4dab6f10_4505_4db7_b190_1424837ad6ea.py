"""Independent 32px profile of users-two-rounded.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4dab6f10-4505-4db7-b190-1424837ad6ea'
SOURCE_PATH = 'pictographic-primitives/symbol/user group_4dab6f10-4505-4db7-b190-1424837ad6ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4dab6f10-4505-4db7-b190-1424837ad6ea', 'pictographic-primitives/symbol/user group_4dab6f10-4505-4db7-b190-1424837ad6ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/users-two-rounded',)
SOLO_SOURCE_ICON_IDS = ('users-two-rounded',)
REFERENCE_EXPORT_SHA256 = '36d09edd47734eec69c887cd9b7067181110f04121c8c35795f32a169570808d'

class Drawing(Sub32):
    icon_id = 'users-two-rounded-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 9), (13, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (13, 9), (5, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (21, 9), (28, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (28, 9), (21, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (2, 24), (16, 24), radius_x=7, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (16, 24), (16, 27))
        self.add_line('p3-r1-3', (16, 27), (2, 27))
        self.add_line('p3-r1-4', (2, 27), (2, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_arc('p4-r1-1', (16, 24), (30, 24), radius_x=7, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p4-r1-2', (30, 24), (30, 27))
        self.add_line('p4-r1-3', (30, 27), (16, 27))
        self.add_line('p4-r1-4', (16, 27), (16, 24))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-4')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-3')
        self.relate("connect", 'p3-r1-2', 'p4-r1-4')
        self.relate("connect", 'p3-r1-3', 'p4-r1-3')
        self.relate("connect", 'p3-r1-3', 'p4-r1-4')
