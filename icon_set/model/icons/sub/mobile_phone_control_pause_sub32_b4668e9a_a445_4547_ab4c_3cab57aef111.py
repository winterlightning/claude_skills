"""Independent 32px profile of mobile-phone-control-pause.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4668e9a-a445-4547-ab4c-3cab57aef111', 'pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-phone-control-pause',)
SOLO_SOURCE_ICON_IDS = ('mobile-phone-control-pause',)
REFERENCE_EXPORT_SHA256 = 'fc287b2033f1f997471d2a1565723715760e86edebee783467b4c541f1728693'

class Drawing(Sub32):
    icon_id = 'mobile-phone-control-pause-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 6), (27, 23))
        self.add_line('p1-r1-4', (27, 23), (27, 26))
        self.add_arc('p1-r1-5', (27, 26), (24, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (24, 30), (8, 30))
        self.add_arc('p1-r1-7', (8, 30), (5, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 26), (5, 23))
        self.add_line('p1-r1-9', (5, 23), (5, 6))
        self.add_arc('p1-r1-10', (5, 6), (8, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (5, 23), (27, 23))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 9), (13, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 9), (20, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
