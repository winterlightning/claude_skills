"""Prescription px (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df777ff5-6e54-5fbd-b667-d76bf10797a0'
SOURCE_PATH = 'icons-json/health/prescription px_df777ff5-6e54-5fbd-b667-d76bf10797a0.json'
AUTHOR = 'json_to_solo'

class PrescriptionPxHealth(Solo48):
    icon_id = 'prescription-px-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('prescription', 'px', 'health')

    def build(self):
        self.add_line('e0', (8, 21), (22, 21))
        self.add_line('e1', (21, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 37))
        self.add_line('e3', (40, 44), (18, 21))
        self.add_line('e4', (21, 44), (40, 25))
        self.add_arc('e5-1', (22, 21), (29, 11), radius_x=8, sweep=False)
        self.add_arc('e5-2', (29, 11), (21, 4), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
