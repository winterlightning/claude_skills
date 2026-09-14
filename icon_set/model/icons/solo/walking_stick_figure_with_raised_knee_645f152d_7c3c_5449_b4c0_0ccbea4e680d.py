'A stick figure steps toward the right with one knee raised and the forward arm bent horizontally. The other arm and leg extend backward beneath the upright torso and circular head.\n\nConstruction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).\nLucide: person-standing: separate round head, common limb junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '645f152d-7c3c-5449-b4c0-0ccbea4e680d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking_645f152d-7c3c-5449-b4c0-0ccbea4e680d.svg'
AUTHOR = 'gpt-6'

class WalkingStickFigureWithRaisedKnee(Solo48):
    icon_id = 'walking-stick-figure-with-raised-knee'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'stick', 'figure', 'knee', 'stride')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (22, 7), (28, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (28, 7), (22, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (24, 19), (22, 31))
        self.add_line('person-arms-1', (8, 29), (14, 21))
        self.add_line('person-arms-2', (14, 21), (24, 19))
        self.add_line('person-arms-3', (24, 19), (30, 27))
        self.add_line('person-arms-4', (30, 27), (40, 29))
        self.add_line('person-legs-1', (10, 44), (20, 37))
        self.add_line('person-legs-2', (20, 37), (22, 31))
        self.add_line('person-legs-3', (22, 31), (36, 36))
        self.add_line('person-legs-4', (36, 36), (38, 44))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', 'person-arms-3', 'person-arms-4', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', 'person-legs-4', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
