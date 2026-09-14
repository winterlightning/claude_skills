"""Circle half (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '031da5e5-a8c4-45af-9b74-e8c1dae95201'
SOURCE_PATH = 'icons-json/symbol/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.json'
AUTHOR = 'json_to_solo'

class CircleHalf031da5e5(Solo48):
    icon_id = 'circle-half-031da5e5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('circle', 'half', 'symbol')

    def build(self):
        self.add_line('e0', (40, 44), (40, 4))
        self.add_arc('e1-1', (40, 4), (39, 4), radius_x=17)
        self.add_arc('e1-2', (39, 4), (26, 6), radius_x=45, sweep=False)
        self.add_arc('e1-3', (26, 6), (23, 7), radius_x=40, sweep=False)
        self.add_arc('e1-4', (23, 7), (8, 24), radius_x=19, sweep=False)
        self.add_arc('e1-5', (8, 24), (19, 39), radius_x=18, sweep=False)
        self.add_arc('e1-6', (19, 39), (26, 42), radius_x=39, sweep=False)
        self.add_line('e1-7', (26, 42), (40, 44))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e0', closed=True)
