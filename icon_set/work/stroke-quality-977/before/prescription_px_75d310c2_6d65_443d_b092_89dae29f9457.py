"""Prescription px (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75d310c2-6d65-443d-b092-89dae29f9457'
SOURCE_PATH = 'pictographic-primitives/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PrescriptionPx(Solo48):
    icon_id = 'prescription-px'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('prescription', 'px', 'health')

    def build(self):
        self.add_line('e0', (8, 37), (8, 4))
        self.add_line('e1', (8, 4), (21, 4))
        self.add_line('e2', (21, 21), (8, 21))
        self.add_line('e3', (21, 44), (31, 35))
        self.add_line('e4', (31, 35), (40, 44))
        self.add_line('e5', (40, 26), (31, 35))
        self.add_line('e6', (31, 35), (17, 21))
        self.add_arc('e7-1', (21, 4), (28, 8), radius_x=9)
        self.add_arc('e7-2', (28, 8), (21, 21), radius_x=9)
        self.add_contour('c0', 'e0', 'e1', 'e7-1', 'e7-2', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.relate('connect', 'c1', 'c2')
