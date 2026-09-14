'A person walks toward the right with a rounded back and lowered head. The arms hang forward near the waist, and the legs separate into a short staggered stride.\n\nConstruction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).\nLucide: person-standing: separate round head, common limb junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '822cd704-4a41-5ae3-98e9-c89f5e699b25'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking stooped_822cd704-4a41-5ae3-98e9-c89f5e699b25.svg'
AUTHOR = 'gpt-6'

class StoopedWalkingPerson(Solo48):
    icon_id = 'stooped-walking-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'stooped', 'posture', 'pedestrian', 'figure')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (29, 7), (35, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (35, 7), (29, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (24, 19), (18, 30))
        self.add_line('person-arms-1', (24, 19), (26, 29))
        self.add_line('person-arms-2', (26, 29), (34, 32))
        self.add_line('person-legs-1', (8, 44), (18, 30))
        self.add_line('person-legs-2', (18, 30), (30, 36))
        self.add_line('person-legs-3', (30, 36), (30, 44))
        self.add_line('person-hand-1', (34, 32), (40, 32))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.add_contour('person-hand', 'person-hand-1', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'person-arms', 'person-hand')
