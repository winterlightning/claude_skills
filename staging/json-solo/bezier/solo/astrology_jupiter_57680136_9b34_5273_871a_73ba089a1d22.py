"""Batch-04/astrology jupiter (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e3', (8, 4), ((9.086, 4), (10.164, 4.018), (11.251, 4.018)), ((12.514, 4.018), (13.836, 4.264), (15.04, 4.673)), ((22.796, 7.309), (20.497, 17.273), (16.716, 22.536)), ((16.126, 23.364), (15.766, 24.336), (15, 25)))
        self.add_contour('c0', 'e3', 'e0', 'e1')
        self.add_contour('c1', 'e2')
