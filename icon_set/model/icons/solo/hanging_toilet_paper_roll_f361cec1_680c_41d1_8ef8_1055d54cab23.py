'A horizontal toilet paper roll has a circular opening visible on its right end. A long sheet hangs over the front with two dotted perforation rows and an uneven curled lower edge.\n\nConstruction: Horizontal roll with a long hanging sheet and torn lower edge; one circular core retained. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f361cec1-680c-41d1-8ef8-1055d54cab23'
SOURCE_PATH = 'pictographic-primitives/wayfinding/toilet paper_f361cec1-680c-41d1-8ef8-1055d54cab23.svg'
AUTHOR = 'gpt-6'

class HangingToiletPaperRoll(Solo48):
    icon_id = 'hanging-toilet-paper-roll'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('toilet', 'paper', 'roll', 'tissue', 'perforation', 'bathroom')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('roll-top', (8, 16), (20, 4), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('roll-roof', (20, 4), (32, 4))
        self.add_arc('roll-end-top', (32, 4), (40, 16), radius_x=8, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('roll-end-bottom', (40, 16), (32, 28), radius_x=8, radius_y=12, large_arc=False, sweep=True)
        self.add_line('sheet-side', (32, 28), (32, 44))
        self.add_line('torn-1', (32, 44), (24, 40))
        self.add_line('torn-2', (24, 40), (16, 44))
        self.add_line('torn-3', (16, 44), (8, 40))
        self.add_line('torn-4', (8, 40), (8, 16))
        self.add_arc('core-top', (25, 16), (31, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('core-bottom', (31, 16), (25, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('outline', 'roll-top', 'roll-roof', 'roll-end-top', 'roll-end-bottom', 'sheet-side', 'torn-1', 'torn-2', 'torn-3', 'torn-4', closed=True)
        self.add_contour('core', 'core-top', 'core-bottom', closed=True)
