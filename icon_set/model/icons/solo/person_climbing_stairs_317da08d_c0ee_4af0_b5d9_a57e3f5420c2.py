'A person faces right and steps onto a short rising staircase. One knee lifts over a step while the rear leg remains lower, and the arms swing beside the torso.\n\nConstruction: Walking figure with one foot on a three-step staircase. Distinct knee and arm positions indicate the direction of travel. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '317da08d-c0ee-4af0-b5d9-a57e3f5420c2'
SOURCE_PATH = 'pictographic-primitives/wayfinding/stairs person ascend_317da08d-c0ee-4af0-b5d9-a57e3f5420c2.svg'
AUTHOR = 'gpt-6'

class PersonClimbingStairs(Solo48):
    icon_id = 'person-climbing-stairs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'stairs', 'ascending', 'climbing', 'steps', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (14, 9), (20, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (20, 9), (14, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (18, 21), (16, 29))
        self.add_line('person-arms-1', (6, 27), (18, 21))
        self.add_line('person-arms-2', (18, 21), (27, 25))
        self.add_line('person-legs-1', (8, 42), (16, 29))
        self.add_line('person-legs-2', (16, 29), (26, 28))
        self.add_line('person-legs-3', (26, 28), (30, 30))
        self.add_line('stairs-1', (20, 42), (20, 36))
        self.add_line('stairs-2', (20, 36), (30, 36))
        self.add_line('stairs-3', (30, 36), (30, 30))
        self.add_line('stairs-4', (30, 30), (36, 30))
        self.add_line('stairs-5', (36, 30), (36, 24))
        self.add_line('stairs-6', (36, 24), (42, 24))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.add_contour('stairs', 'stairs-1', 'stairs-2', 'stairs-3', 'stairs-4', 'stairs-5', 'stairs-6', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'stairs', 'person-legs')
