'A person sits in profile with a circular head above a backward-sloping torso. One arm extends forward horizontally and the legs bend together beneath the body without a visible chair.\n\nConstruction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).\nLucide: person-standing: separate round head, common limb junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29bfafb8-d4e4-426a-8a48-2a24f5d6af8d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/sitting_29bfafb8-d4e4-426a-8a48-2a24f5d6af8d.svg'
AUTHOR = 'gpt-6'

class SeatedPerson(Solo48):
    icon_id = 'seated-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'seated', 'sitting', 'posture', 'rest', 'figure')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (21, 7), (27, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (27, 7), (21, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (20, 19), (16, 34))
        self.add_line('person-torso-2', (16, 34), (26, 34))
        self.add_line('person-torso-3', (26, 34), (36, 44))
        self.add_line('person-arm-1', (20, 19), (40, 19))
        self.add_line('person-foot-1', (16, 34), (8, 44))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', 'person-torso-2', 'person-torso-3', closed=False)
        self.add_contour('person-arm', 'person-arm-1', closed=False)
        self.add_contour('person-foot', 'person-foot-1', closed=False)
        self.relate('connect', 'person-torso', 'person-arm')
        self.relate('connect', 'person-torso', 'person-foot')
