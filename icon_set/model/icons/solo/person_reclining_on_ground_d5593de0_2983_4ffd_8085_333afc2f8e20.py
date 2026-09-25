'A seated person leans backward on one arm with the knees raised. The torso angles toward the round head, and the bent legs stretch across the lower-right side.\n\nConstruction: Reclining seated figure supports the body with one arm and raises both knees. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5593de0-2983-4ffd-8085-333afc2f8e20'
SOURCE_PATH = 'pictographic-primitives/wayfinding/sitting relax_d5593de0-2983-4ffd-8085-333afc2f8e20.svg'
AUTHOR = 'gpt-6'

class PersonRecliningOnGround(Solo48):
    icon_id = 'person-reclining-on-ground'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'reclining', 'sitting', 'rest', 'ground', 'relax')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (11, 11), (17, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (17, 11), (11, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (16, 23), (22, 40))
        self.add_line('person-arm-1', (16, 23), (10, 40))
        self.add_line('person-arm-2', (10, 40), (4, 40))
        self.add_line('person-legs-1', (22, 40), (34, 24))
        self.add_line('person-legs-2', (34, 24), (44, 36))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arm', 'person-arm-1', 'person-arm-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.relate('connect', 'person-torso', 'person-arm')
        self.relate('connect', 'person-torso', 'person-legs')
