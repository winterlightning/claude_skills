'A person runs toward the right with a forward-leaning torso and a circular head. One arm reaches ahead, the other bends behind, and the rear leg stretches diagonally backward.\n\nConstruction: Runner leaning right with bent arms and a long trailing leg. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'faa8ce36-0bcb-5aa9-9171-0fa6b6ee89eb'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety exit right_faa8ce36-0bcb-5aa9-9171-0fa6b6ee89eb.svg'
AUTHOR = 'gpt-6'

class PersonRunningRight(Solo48):
    icon_id = 'person-running-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'running', 'right', 'escape', 'motion', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (29, 9), (35, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (35, 9), (29, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (28, 21), (22, 29))
        self.add_line('person-arms-1', (12, 25), (18, 19))
        self.add_line('person-arms-2', (18, 19), (28, 21))
        self.add_line('person-arms-3', (28, 21), (32, 29))
        self.add_line('person-arms-4', (32, 29), (42, 29))
        self.add_line('person-legs-1', (6, 42), (22, 29))
        self.add_line('person-legs-2', (22, 29), (30, 36))
        self.add_line('person-legs-3', (30, 36), (26, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', 'person-arms-3', 'person-arms-4', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.relate('connect', 'person-torso', 'person-arms')
        self.relate('connect', 'person-torso', 'person-legs')
