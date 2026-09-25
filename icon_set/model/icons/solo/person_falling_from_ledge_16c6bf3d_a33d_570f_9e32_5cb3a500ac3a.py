'A person tumbles diagonally down and right beside a short squared ledge at lower-left. The limbs splay away from the tilted torso, with the round head above the right shoulder.\n\nConstruction: Tumbling person with splayed limbs beside a squared ledge. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16c6bf3d-a33d-570f-9e32-5cb3a500ac3a'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety danger cliff_16c6bf3d-a33d-570f-9e32-5cb3a500ac3a.svg'
AUTHOR = 'gpt-6'

class PersonFallingFromLedge(Solo48):
    icon_id = 'person-falling-from-ledge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('falling', 'person', 'ledge', 'cliff', 'danger', 'safety')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (30, 9), (36, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (36, 9), (30, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (26, 21), (20, 29))
        self.add_line('person-arms-1', (14, 15), (26, 21))
        self.add_line('person-arms-2', (26, 21), (42, 29))
        self.add_line('person-legs-1', (10, 27), (20, 29))
        self.add_line('person-legs-2', (20, 29), (24, 35))
        self.add_line('person-legs-3', (24, 35), (18, 42))
        self.add_line('ledge-1', (6, 36), (10, 36))
        self.add_line('ledge-2', (10, 36), (10, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.add_contour('ledge', 'ledge-1', 'ledge-2', closed=False)
        self.relate('connect', 'person-torso', 'person-arms')
        self.relate('connect', 'person-torso', 'person-legs')
