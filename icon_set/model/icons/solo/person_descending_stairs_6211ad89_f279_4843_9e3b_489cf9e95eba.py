'A person stands across two levels of a short staircase with the front leg reaching toward the lower left. The arms bend beside a nearly upright torso and circular head.\n\nConstruction: Walking figure with one foot on a three-step staircase. Distinct knee and arm positions indicate the direction of travel. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6211ad89-f279-4843-9e3b-489cf9e95eba'
SOURCE_PATH = 'pictographic-primitives/wayfinding/stairs person decend_6211ad89-f279-4843-9e3b-489cf9e95eba.svg'
AUTHOR = 'gpt-6'

class PersonDescendingStairs(Solo48):
    icon_id = 'person-descending-stairs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'stairs', 'descending', 'steps', 'walking', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (19, 9), (25, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (25, 9), (19, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (18, 21), (22, 29))
        self.add_line('person-arms-1', (6, 25), (18, 21))
        self.add_line('person-arms-2', (18, 21), (28, 26))
        self.add_line('person-legs-1', (12, 40), (22, 29))
        self.add_line('person-legs-2', (22, 29), (30, 36))
        self.add_line('stairs-1', (20, 42), (20, 36))
        self.add_line('stairs-2', (20, 36), (30, 36))
        self.add_line('stairs-3', (30, 36), (30, 30))
        self.add_line('stairs-4', (30, 30), (36, 30))
        self.add_line('stairs-5', (36, 30), (36, 24))
        self.add_line('stairs-6', (36, 24), (42, 24))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.add_contour('stairs', 'stairs-1', 'stairs-2', 'stairs-3', 'stairs-4', 'stairs-5', 'stairs-6', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'stairs', 'person-legs')
