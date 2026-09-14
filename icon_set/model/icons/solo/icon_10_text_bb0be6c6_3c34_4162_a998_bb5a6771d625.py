"""10 (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb0be6c6-3c34-4162-a998-bb5a6771d625'
SOURCE_PATH = 'icons-json/other/10 (text)_bb0be6c6-3c34-4162-a998-bb5a6771d625.json'
AUTHOR = 'json_to_solo'

class Icon10Text(Solo48):
    icon_id = 'icon-10-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (11, 8), (11, 40))
        self.add_bezier('e1', (4, 14), ((4.009, 14), (4.009, 13.99), (4.018, 13.99)), ((4.018, 13.96), (4.509, 13.75), (4.536, 13.74)), ((5.4, 13.32), (6.236, 12.83), (7.027, 12.28)), ((8.673, 11.14), (9.655, 9.5), (11, 8)))
        self.add_bezier('e2', (24, 24), ((24.045, 18.74), (24.955, 12.44), (29.336, 9.34)), ((30.409, 8.59), (31.773, 8.02), (33.064, 8.02)), ((33.245, 8.02), (33.436, 8), (33.618, 8)), ((33.8, 8), (33.991, 8.02), (34.173, 8.02)), ((40.364, 8.02), (43.991, 16.64), (43.991, 22.58)), ((43.991, 22.88), (44, 23.19), (44, 23.5)), ((44, 23.67), (44, 23.83), (44, 24)))
        self.add_bezier('e3', (44, 24), ((44, 24.37), (43.991, 24.75), (43.991, 25.12)), ((43.991, 30.89), (40.982, 39.98), (34.736, 39.98)), ((34.555, 39.98), (34.364, 40), (34.182, 40)), ((34, 40), (33.809, 39.98), (33.627, 39.98)), ((32.336, 39.98), (30.973, 39.48), (29.864, 38.78)), ((25.273, 35.87), (24.009, 29.38), (24, 24)))
        self.add_contour('c0', 'e1', 'e0')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
