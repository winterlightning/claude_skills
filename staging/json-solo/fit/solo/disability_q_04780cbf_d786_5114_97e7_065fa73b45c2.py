"""Disability q (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04780cbf-d786-5114-97e7-065fa73b45c2'
SOURCE_PATH = 'icons-json/typeface/disability q_04780cbf-d786-5114-97e7-065fa73b45c2.json'
AUTHOR = 'json_to_solo'

class DisabilityQTypeface(Solo48):
    icon_id = 'disability-q-typeface'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('disability', 'q', 'typeface')

    def build(self):
        self.add_line('e0', (31, 30), (37, 36))
        self.add_line('e1', (29, 7), (25, 6))
        self.add_line('e2', (37, 36), (42, 41))
        self.add_arc('e3-1', (37, 36), (42, 24), radius_x=20, sweep=False)
        self.add_arc('e3-2', (42, 24), (29, 7), radius_x=18, sweep=False)
        self.add_line('e4-1', (25, 6), (18, 7))
        self.add_arc('e4-2', (18, 7), (6, 24), radius_x=19, sweep=False)
        self.add_arc('e4-3', (6, 24), (24, 42), radius_x=18, sweep=False)
        self.add_arc('e4-4', (24, 42), (37, 36), radius_x=18, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e2')
