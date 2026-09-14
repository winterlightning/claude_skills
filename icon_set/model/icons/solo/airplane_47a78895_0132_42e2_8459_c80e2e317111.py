"""Airplane (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47a78895-0132-42e2-8459-c80e2e317111'
SOURCE_PATH = 'icons-json/other/airplane_47a78895-0132-42e2-8459-c80e2e317111.json'
AUTHOR = 'json_to_solo'

class Airplane(Solo48):
    icon_id = 'airplane'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('airplane', 'other')

    def build(self):
        self.add_line('e0', (4, 28), (11, 39))
        self.add_line('e1', (18, 39), (41, 20))
        self.add_line('e2', (29, 15), (17, 8))
        self.add_line('e3', (16, 8), (12, 11))
        self.add_line('e4', (12, 11), (20, 23))
        self.add_line('e5', (20, 23), (14, 28))
        self.add_line('e6', (14, 28), (8, 25))
        self.add_line('e7', (8, 25), (4, 28))
        self.add_line('e8-1', (11, 39), (14, 40))
        self.add_line('e8-2', (14, 40), (18, 39))
        self.add_line('e9-1', (41, 20), (43, 17))
        self.add_line('e9-2', (43, 17), (44, 13))
        self.add_arc('e9-3', (44, 13), (39, 8), radius_x=5, sweep=False)
        self.add_arc('e9-4', (39, 8), (29, 15), radius_x=19, sweep=False)
        self.add_line('e10', (17, 8), (16, 8))
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e2', 'e10', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
