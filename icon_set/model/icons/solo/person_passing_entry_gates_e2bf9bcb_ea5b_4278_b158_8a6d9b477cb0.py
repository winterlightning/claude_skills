'A front-facing person stands between two short rectangular gate posts. The figure has a circular head above a rounded torso and close-set legs, with open space on either side.\n\nConstruction: Standing visitor between two waist-high entry gate posts. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2bf9bcb-ea5b-4278-b158-8a6d9b477cb0'
SOURCE_PATH = 'pictographic-primitives/wayfinding/ticket person pass_e2bf9bcb-ea5b-4278-b158-8a6d9b477cb0.svg'
AUTHOR = 'gpt-6'

class PersonPassingEntryGates(Solo48):
    icon_id = 'person-passing-entry-gates'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'gates', 'entry', 'admission', 'pass', 'access')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (24, 21), (24, 32))
        self.add_line('person-body-2', (24, 32), (22, 42))
        self.add_line('person-leg-1', (24, 32), (26, 42))
        self.add_line('left-gate-0', (8, 24), (12, 24))
        self.add_arc('left-gate-1', (12, 24), (14, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('left-gate-2', (14, 26), (14, 40))
        self.add_arc('left-gate-3', (14, 40), (12, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('left-gate-4', (12, 42), (8, 42))
        self.add_arc('left-gate-5', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('left-gate-6', (6, 40), (6, 26))
        self.add_arc('left-gate-7', (6, 26), (8, 24), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('right-gate-0', (36, 24), (40, 24))
        self.add_arc('right-gate-1', (40, 24), (42, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('right-gate-2', (42, 26), (42, 40))
        self.add_arc('right-gate-3', (42, 40), (40, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('right-gate-4', (40, 42), (36, 42))
        self.add_arc('right-gate-5', (36, 42), (34, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('right-gate-6', (34, 40), (34, 26))
        self.add_arc('right-gate-7', (34, 26), (36, 24), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', closed=False)
        self.add_contour('person-leg', 'person-leg-1', closed=False)
        self.add_contour('left-gate', 'left-gate-0', 'left-gate-1', 'left-gate-2', 'left-gate-3', 'left-gate-4', 'left-gate-5', 'left-gate-6', 'left-gate-7', closed=True)
        self.add_contour('right-gate', 'right-gate-0', 'right-gate-1', 'right-gate-2', 'right-gate-3', 'right-gate-4', 'right-gate-5', 'right-gate-6', 'right-gate-7', closed=True)
        self.relate('connect', 'person-body', 'person-leg')
