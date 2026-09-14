'A person pitches forward toward the right with one arm extended and the rear leg stretched behind. A small angular rock sits just ahead of the lowered front foot.\n\nConstruction: Runner pitching forward toward a small triangular obstacle. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33343e0b-3052-52e7-b5fb-b5849fef9eaf'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety rocky road_33343e0b-3052-52e7-b5fb-b5849fef9eaf.svg'
AUTHOR = 'gpt-6'

class PersonTrippingOverRock(Solo48):
    icon_id = 'person-tripping-over-rock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('tripping', 'person', 'rock', 'hazard', 'fall', 'safety')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (25, 9), (31, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (31, 9), (25, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (24, 21), (18, 30))
        self.add_line('person-arms-1', (12, 27), (18, 21))
        self.add_line('person-arms-2', (18, 21), (24, 21))
        self.add_line('person-arms-3', (24, 21), (34, 29))
        self.add_line('person-legs-1', (6, 37), (18, 30))
        self.add_line('person-legs-2', (18, 30), (24, 35))
        self.add_line('person-legs-3', (24, 35), (20, 42))
        self.add_line('rock-1', (34, 42), (38, 37))
        self.add_line('rock-2', (38, 37), (42, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', 'person-arms-3', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.add_contour('rock', 'rock-1', 'rock-2', closed=False)
        self.relate('connect', 'person-torso', 'person-arms')
        self.relate('connect', 'person-torso', 'person-legs')
