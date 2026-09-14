"""Slash heart (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6e7fb81-1452-4bf0-9940-ca1bd392e448'
SOURCE_PATH = 'icons-json/symbol/slash heart_f6e7fb81-1452-4bf0-9940-ca1bd392e448.json'
AUTHOR = 'json_to_solo'

class SlashHeartSymbol(Solo48):
    icon_id = 'slash-heart-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('slash', 'heart', 'symbol')

    def build(self):
        self.add_line('e0', (39, 39), (6, 8))
        self.add_line('e1', (7, 24), (24, 40))
        self.add_line('e2', (24, 40), (41, 24))
        self.add_bezier('e3', (41, 24), ((42.391, 22.712), (43.982, 19.924), (43.982, 18.055)), ((43.991, 17.962), (43.991, 17.878), (44, 17.785)), ((44, 17.782), (44, 17.779), (44, 17.777)), ((44, 17.594), (43.982, 17.412), (43.982, 17.229)), ((43.982, 16.126), (43.518, 14.947), (43.036, 13.954)), ((40.591, 8.926), (34.373, 8), (29.1, 9.373)), ((27.718, 9.962), (26.527, 10.813), (25.491, 11.84)), ((24.991, 12.337), (24.5, 12.825), (24, 13.322)), ((23.364, 12.707), (22.727, 12.093), (22.091, 11.478)), ((21.127, 10.543), (19.927, 9.794), (18.636, 9.305)), ((13.127, 8), (7.636, 9.137), (5.055, 14.004)), ((4.482, 15.099), (4, 16.025), (4, 17.288)), ((4, 17.291), (4, 17.294), (4, 17.297)), ((4, 17.479), (4.009, 17.662), (4.009, 17.853)), ((4.009, 19.512), (5.755, 22.846), (7, 24)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=True)
