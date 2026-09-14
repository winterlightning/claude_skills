"""Q (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e40e093e-f5b4-5416-8ac1-2cb3ee5d6d0d'
SOURCE_PATH = 'icons-json/typeface/Q_e40e093e-f5b4-5416-8ac1-2cb3ee5d6d0d.json'
AUTHOR = 'json_to_solo'

class QE40e093e(Solo48):
    icon_id = 'q-e40e093e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('q', 'typeface')

    def build(self):
        self.add_line('e0', (8, 14), (8, 29))
        self.add_line('e1-1', (28, 38), (29, 42))
        self.add_arc('e1-2', (29, 42), (35, 44), radius_x=10, sweep=False)
        self.add_arc('e2-1', (28, 38), (37, 34), radius_x=18, sweep=False)
        self.add_arc('e2-2', (37, 34), (40, 28), radius_x=9, sweep=False)
        self.add_line('e2-3', (40, 28), (40, 18))
        self.add_line('e2-4', (40, 18), (39, 11))
        self.add_arc('e2-5', (39, 11), (34, 6), radius_x=11, sweep=False)
        self.add_line('e2-6', (34, 6), (24, 4))
        self.add_line('e2-7', (24, 4), (14, 6))
        self.add_arc('e2-8', (14, 6), (8, 14), radius_x=10, sweep=False)
        self.add_arc('e3-1', (8, 29), (17, 37), radius_x=12, sweep=False)
        self.add_arc('e3-2', (17, 37), (28, 38), radius_x=36, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e0', 'e3-1', 'e3-2')
