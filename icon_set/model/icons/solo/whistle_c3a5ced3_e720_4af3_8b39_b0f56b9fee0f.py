"""Whistle (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3a5ced3-e720-4af3-8b39-b0f56b9fee0f'
SOURCE_PATH = 'icons-json/sports/whistle_c3a5ced3-e720-4af3-8b39-b0f56b9fee0f.json'
AUTHOR = 'json_to_solo'

class WhistleSports(Solo48):
    icon_id = 'whistle-sports'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('whistle', 'sports')

    def build(self):
        self.add_line('e0', (40, 6), (42, 13))
        self.add_line('e1', (42, 13), (31, 22))
        self.add_line('e2', (13, 17), (40, 6))
        self.add_bezier('e3', (31, 22), ((31.982, 24.741), (33.106, 26.929), (32.795, 29.883)), ((32.125, 36.338), (26.569, 41.992), (19.893, 41.992)), ((19.716, 41.992), (19.546, 42), (19.369, 42)), ((19.367, 42), (19.364, 42), (19.361, 42)), ((12.39, 42), (6.008, 35.831), (6.008, 28.778)), ((6.008, 28.601), (6, 28.432), (6, 28.255)), ((6, 28.252), (6, 28.249), (6, 28.246)), ((6, 24.196), (7.98, 20.31), (11.253, 17.921)), ((11.891, 17.446), (12.255, 17.303), (13, 17)))
        self.add_contour('c0', 'e0', 'e1', 'e3', 'e2', closed=True)
