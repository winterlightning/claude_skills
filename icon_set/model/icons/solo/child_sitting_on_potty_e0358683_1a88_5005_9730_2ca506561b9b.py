"A small person sits facing right on a low potty with a tall back and arched opening at the base. The child's arms bend forward above the thighs and hanging legs.\n\nConstruction: Small seated child above a low potty seat. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0358683-1a88-5005-9730-2ca506561b9b'
SOURCE_PATH = 'pictographic-primitives/wayfinding/urinal baby sit_e0358683-1a88-5005-9730-2ca506561b9b.svg'
AUTHOR = 'gpt-6'

class ChildSittingOnPotty(Solo48):
    icon_id = 'child-sitting-on-potty'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('child', 'potty', 'toilet', 'seated', 'baby', 'bathroom')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (19, 7), (25, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (25, 7), (19, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (20, 19), (18, 30))
        self.add_line('person-body-2-joint-1', (18, 30), (24, 30))
        self.add_line('person-body-2-joint-2', (24, 30), (30, 30))
        self.add_line('person-body-3', (30, 30), (40, 40))
        self.add_line('person-arm-1', (20, 19), (32, 24))
        self.add_line('potty-1', (8, 30), (18, 30))
        self.add_line('potty-2', (18, 30), (24, 30))
        self.add_line('potty-3', (24, 30), (24, 44))
        self.add_line('potty-4', (24, 44), (8, 44))
        self.add_line('potty-5', (8, 44), (8, 30))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2-joint-1', 'person-body-2-joint-2', 'person-body-3', closed=False)
        self.add_contour('person-arm', 'person-arm-1', closed=False)
        self.add_contour('potty', 'potty-1', 'potty-2', 'potty-3', 'potty-4', 'potty-5', closed=True)
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'potty', 'person-body')
