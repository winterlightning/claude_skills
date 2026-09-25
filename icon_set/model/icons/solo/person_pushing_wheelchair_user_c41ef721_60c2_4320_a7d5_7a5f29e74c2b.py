"A standing helper leans forward behind a seated wheelchair user facing right. The helper's hands meet the chair back, while the seated figure's bent legs extend beyond the large rear wheel.\n\nConstruction: Standing helper pushes a seated wheelchair user; chair wheel is an open arc to preserve limb clearance. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c41ef721-60c2-4320-a7d5-7a5f29e74c2b'
SOURCE_PATH = 'pictographic-primitives/wayfinding/wheelchair helper_c41ef721-60c2-4320-a7d5-7a5f29e74c2b.svg'
AUTHOR = 'gpt-6'

class PersonPushingWheelchairUser(Solo48):
    icon_id = 'person-pushing-wheelchair-user'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('wheelchair', 'helper', 'person', 'assistance', 'mobility', 'accessibility')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('helper-head-top', (9, 11), (15, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('helper-head-bottom', (15, 11), (9, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('helper-body-1', (12, 23), (10, 31))
        self.add_line('helper-arm-1', (12, 23), (30, 25))
        self.add_line('helper-legs-1', (4, 40), (10, 31))
        self.add_line('helper-legs-2', (10, 31), (16, 40))
        self.add_arc('rider-head-top', (29, 11), (35, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('rider-head-bottom', (35, 11), (29, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('rider-body-1', (30, 23), (30, 25))
        self.add_line('rider-body-2', (30, 25), (30, 31))
        self.add_line('rider-body-3', (30, 31), (38, 31))
        self.add_line('rider-body-4', (38, 31), (44, 40))
        self.add_arc('wheel', (30, 25), (30, 39), radius_x=8, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('helper-head', 'helper-head-top', 'helper-head-bottom', closed=True)
        self.add_contour('helper-body', 'helper-body-1', closed=False)
        self.add_contour('helper-arm', 'helper-arm-1', closed=False)
        self.add_contour('helper-legs', 'helper-legs-1', 'helper-legs-2', closed=False)
        self.add_contour('rider-head', 'rider-head-top', 'rider-head-bottom', closed=True)
        self.add_contour('rider-body', 'rider-body-1', 'rider-body-2', 'rider-body-3', 'rider-body-4', closed=False)
        self.relate('connect', 'helper-body', 'helper-arm')
        self.relate('connect', 'helper-body', 'helper-legs')
        self.relate('connect', 'wheel', 'rider-body')
        self.relate('connect', 'wheel', 'helper-arm')
