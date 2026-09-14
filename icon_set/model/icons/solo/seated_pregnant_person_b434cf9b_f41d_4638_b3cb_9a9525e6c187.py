'A pregnant person sits facing right on a curved-backed seat. The rounded belly projects prominently above the bent thighs, while the lower leg drops in front of the seat.\n\nConstruction: Seated profile with rounded abdomen and a simple chair back. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b434cf9b-f41d-4638-b3cb-9a9525e6c187'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability sit pregnancy_b434cf9b-f41d-4638-b3cb-9a9525e6c187.svg'
AUTHOR = 'gpt-6'

class SeatedPregnantPerson(Solo48):
    icon_id = 'seated-pregnant-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('pregnant', 'seated', 'pregnancy', 'maternity', 'chair', 'person')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (17, 7), (23, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (23, 7), (17, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('back-and-leg-1', (18, 19), (20, 32))
        self.add_line('back-and-leg-2', (20, 32), (32, 32))
        self.add_line('back-and-leg-3', (32, 32), (36, 44))
        self.add_arc('belly', (18, 19), (40, 34), radius_x=22, radius_y=15, large_arc=False, sweep=True)
        self.add_line('front-leg', (40, 34), (40, 44))
        self.add_line('chair-1', (8, 23), (8, 42))
        self.add_line('chair-2', (8, 42), (22, 42))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('back-and-leg', 'back-and-leg-1', 'back-and-leg-2', 'back-and-leg-3', closed=False)
        self.add_contour('abdomen', 'belly', 'front-leg', closed=False)
        self.add_contour('chair', 'chair-1', 'chair-2', closed=False)
        self.relate('connect', 'back-and-leg', 'abdomen')
