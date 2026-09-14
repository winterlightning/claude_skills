"""Batch-04/astrology jupiter (culture), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57680136-9b34-5273-871a-73ba089a1d22'
SOURCE_PATH = 'icons-json/culture/batch-04/astrology jupiter_57680136-9b34-5273-871a-73ba089a1d22.json'
AUTHOR = 'json_to_solo'

class Batch04AstrologyJupiter(Solo48):
    icon_id = 'batch-04-astrology-jupiter'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'jupiter', 'culture')

    def build(self):
        self.add_line('e0', (15, 25), (11, 29))
        self.add_line('e1', (11, 29), (40, 29))
        self.add_line('e2', (32, 12), (32, 44))
        self.add_line('e3-1', (8, 4), (16, 5))
        self.add_arc('e3-2', (16, 5), (20, 10), radius_x=7)
        self.add_arc('e3-3', (20, 10), (15, 25), radius_x=19)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e0', 'e1')
        self.add_contour('c1', 'e2')
