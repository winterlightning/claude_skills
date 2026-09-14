'A person faces right and walks along a ground line sloping downward in that direction. One foot rests ahead on the incline while the other trails behind the leaning torso.\n\nConstruction: Walking person on a downward-sloping ground line. Feet share actual ground attachment points. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3784f07-e09a-57a7-a89e-249e8d5c4a3c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking descend_e3784f07-e09a-57a7-a89e-249e8d5c4a3c.svg'
AUTHOR = 'gpt-6'

class PersonWalkingDownSlope(Solo48):
    icon_id = 'person-walking-down-slope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'slope', 'downhill', 'descent', 'pedestrian')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (22, 21), (20, 29))
        self.add_line('person-arms-1', (10, 26), (22, 21))
        self.add_line('person-arms-2', (22, 21), (32, 25))
        self.add_line('person-legs-1', (12, 37), (20, 29))
        self.add_line('person-legs-2', (20, 29), (30, 40))
        self.add_line('slope-1', (6, 36), (12, 37))
        self.add_line('slope-2', (12, 37), (30, 40))
        self.add_line('slope-3', (30, 40), (42, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.add_contour('slope', 'slope-1', 'slope-2', 'slope-3', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'slope', 'person-legs')
