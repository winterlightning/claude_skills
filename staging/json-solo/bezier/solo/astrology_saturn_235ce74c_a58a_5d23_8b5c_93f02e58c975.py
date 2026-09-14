"""Batch-06/astrology saturn (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '235ce74c-a58a-5d23-8b5c-93f02e58c975'
SOURCE_PATH = 'icons-json/culture/batch-06/astrology saturn_235ce74c-a58a-5d23-8b5c-93f02e58c975.json'
AUTHOR = 'json_to_solo'

class Batch06AstrologySaturn(Solo48):
    icon_id = 'batch-06-astrology-saturn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'saturn', 'culture')

    def build(self):
        self.add_line('e0', (17, 21), (17, 4))
        self.add_line('e1', (8, 10), (29, 10))
        self.add_bezier('e2', (19, 44), ((27.948, 42.927), (34.942, 38.7), (38.351, 32.509)), ((39.225, 30.9), (39.975, 29.136), (39.975, 27.382)), ((39.975, 27.087), (40, 26.782), (40, 26.478)), ((40, 26.473), (40, 26.468), (40, 26.464)), ((40, 26.255), (39.975, 26.045), (39.975, 25.836)), ((39.975, 20.609), (34.018, 16.836), (27.077, 17.445)), ((22.978, 17.809), (20.188, 19.191), (17, 21)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e1')
