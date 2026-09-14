'A person strides toward the right with a circular head and slightly forward-leaning torso. One arm bends ahead, the other swings back, and the legs spread widely below.\n\nConstruction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).\nLucide: person-standing: separate round head, common limb junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3fa61ac-129f-4215-bc78-72af508b4c04'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking fast_d3fa61ac-129f-4215-bc78-72af508b4c04.svg'
AUTHOR = 'gpt-6'

class WalkingPerson(Solo48):
    icon_id = 'walking-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'stride', 'pedestrian', 'movement', 'figure')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (23, 7), (29, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (29, 7), (23, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (26, 19), (22, 31))
        self.add_line('person-arms-1', (8, 28), (26, 19))
        self.add_line('person-arms-2', (26, 19), (40, 26))
        self.add_line('person-legs-1', (10, 44), (22, 31))
        self.add_line('person-legs-2', (22, 31), (34, 44))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
