"""Independent 32px profile of rocket-arched-cockpit.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ad6d675e-d8a3-4b65-a826-4422da00e7fa'
SOURCE_PATH = 'pictographic-primitives/science/rocket base_ad6d675e-d8a3-4b65-a826-4422da00e7fa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ad6d675e-d8a3-4b65-a826-4422da00e7fa', 'pictographic-primitives/science/rocket base_ad6d675e-d8a3-4b65-a826-4422da00e7fa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rocket-arched-cockpit',)
SOLO_SOURCE_ICON_IDS = ('rocket-arched-cockpit',)
REFERENCE_EXPORT_SHA256 = 'f6eac61df5c8a817c1883d5a14b1caadca7e83cd081424725738b914aa04f748'

class Drawing(Sub32):
    icon_id = 'rocket-arched-cockpit-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/science'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (24, 12), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (24, 12), (24, 16))
        self.add_line('p1-r1-3', (24, 16), (27, 24))
        self.add_line('p1-r1-4', (27, 24), (19, 24))
        self.add_arc('p1-r1-5', (19, 24), (16, 26), radius_x=3.3541019662496847, radius_y=1.118033988749895, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 26), (13, 24), radius_x=3.3541019662496847, radius_y=1.118033988749895, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (13, 24), (5, 24))
        self.add_line('p1-r1-8', (5, 24), (8, 16))
        self.add_line('p1-r1-9', (8, 16), (8, 12))
        self.add_arc('p1-r1-10', (8, 12), (16, 2), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_arc('p2-r1-1', (14, 16), (18, 16), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 26), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
