"A swimmer's round head and bent raised arm emerge above two rows of waves. The arm reaches over the head toward the right, while the shoulder slopes down toward the water at left.\n\nConstruction: Sideways head and a bent recovery arm above water. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '617863ba-0e98-4490-b124-3f5bfbcb0bb1'
SOURCE_PATH = 'pictographic-primitives/wayfinding/swimming pool person_617863ba-0e98-4490-b124-3f5bfbcb0bb1.svg'
AUTHOR = 'gpt-6'

class Swimmer(Solo48):
    icon_id = 'swimmer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('swimmer', 'swimming', 'pool', 'water', 'arm', 'sport')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (32, 23), (44, 23), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (44, 23), (32, 23), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('arm-1', (10, 26), (18, 22))
        self.add_line('arm-2', (18, 22), (14, 12))
        self.add_line('arm-3', (14, 12), (32, 8))
        self.add_arc('water-0', (4, 38), (14, 38), radius_x=5, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-1', (14, 38), (24, 38), radius_x=5, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('water-2', (24, 38), (34, 38), radius_x=5, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-3', (34, 38), (44, 38), radius_x=5, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('arm', 'arm-1', 'arm-2', 'arm-3', closed=False)
        self.add_contour('water', 'water-0', 'water-1', 'water-2', 'water-3', closed=False)
