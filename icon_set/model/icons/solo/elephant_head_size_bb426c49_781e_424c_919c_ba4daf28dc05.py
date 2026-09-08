"""elephant-head-profile: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb426c49-781e-424c-919c-ba4daf28dc05'
SOURCE_PATH = 'pictographic-primitives/animals/elephant head size_bb426c49-781e-424c-919c-ba4daf28dc05.svg'
AUTHOR = 'gpt-6'


class ElephantHeadProfile(Solo48):
    icon_id = 'elephant-head-profile'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('elephant', 'head', 'profile', 'trunk', 'tusk', 'ear', 'animal', 'wildlife')

    def build(self):
        self.add_arc('head-trunk-1', (2, 12), (14, 5), radius_x=12, radius_y=7, sweep=True)
        self.add_arc('head-trunk-2', (14, 5), (29, 20), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('head-trunk-3', (29, 20), (35, 26), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('head-trunk-4', (35, 26), (39, 22), radius_x=4, radius_y=4, sweep=False)
        self.add_arc('head-trunk-5', (39, 22), (38, 7), radius_x=30, radius_y=30, sweep=False)
        self.add_line('head-trunk-6', (38, 7), (44, 8))
        self.add_arc('head-trunk-7', (44, 8), (46, 18), radius_x=2, radius_y=10, sweep=True)
        self.add_arc('head-trunk-8', (46, 18), (34, 36), radius_x=12, radius_y=18, sweep=True)
        self.add_line('head-trunk-9', (34, 36), (24, 33))
        self.add_contour('head-trunk', 'head-trunk-1', 'head-trunk-2', 'head-trunk-3', 'head-trunk-4', 'head-trunk-5', 'head-trunk-6', 'head-trunk-7', 'head-trunk-8', 'head-trunk-9', closed=False)
        self.add_arc('ear-1', (13, 15), (2, 32), radius_x=11, radius_y=17, sweep=True)
        self.add_contour('ear', 'ear-1', closed=False)
        self.add_arc('jaw-1', (24, 33), (16, 36), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('jaw-2', (16, 36), (10, 43), radius_x=6, radius_y=7, sweep=False)
        self.add_contour('jaw', 'jaw-1', 'jaw-2', closed=False)
        self.relate("connect", 'jaw', 'head-trunk')
        self.add_arc('tusk-1', (24, 33), (35, 43), radius_x=14, radius_y=14, sweep=False)
        self.add_contour('tusk', 'tusk-1', closed=False)
        self.relate("connect", 'tusk', 'head-trunk')
        self.relate("connect", 'tusk', 'jaw')
        self.add_dot('eye', (22, 20))
