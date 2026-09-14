"""66 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71e1e7d3-b065-4190-ab06-ebf4e384b98d'
SOURCE_PATH = 'icons-json/other/66 (text)_71e1e7d3-b065-4190-ab06-ebf4e384b98d.json'
AUTHOR = 'json_to_solo'

class Icon66TextOther(Solo48):
    icon_id = 'icon-66-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_arc('e0-1', (19, 13), (12, 8), radius_x=8, sweep=False)
        self.add_arc('e0-2', (12, 8), (5, 15), radius_x=9, sweep=False)
        self.add_line('e0-3', (5, 15), (4, 24))
        self.add_line('e0-4', (4, 24), (4, 29))
        self.add_arc('e1-1', (43, 13), (37, 8), radius_x=7, sweep=False)
        self.add_arc('e1-2', (37, 8), (30, 15), radius_x=9, sweep=False)
        self.add_line('e1-3', (30, 15), (29, 29))
        self.add_line('e2-1', (4, 29), (6, 37))
        self.add_arc('e2-2', (6, 37), (8, 39), radius_x=8, sweep=False)
        self.add_line('e2-3', (8, 39), (12, 40))
        self.add_arc('e2-4', (12, 40), (17, 23), radius_x=11, sweep=False)
        self.add_arc('e2-5', (17, 23), (11, 20), radius_x=6, sweep=False)
        self.add_arc('e2-6', (11, 20), (4, 29), radius_x=10, sweep=False)
        self.add_arc('e3-1', (29, 29), (32, 38), radius_x=15, sweep=False)
        self.add_line('e3-2', (32, 38), (37, 40))
        self.add_arc('e3-3', (37, 40), (42, 37), radius_x=6, sweep=False)
        self.add_line('e3-4', (42, 37), (44, 30))
        self.add_line('e3-5', (44, 30), (42, 23))
        self.add_arc('e3-6', (42, 23), (37, 20), radius_x=6, sweep=False)
        self.add_arc('e3-7', (37, 20), (32, 22), radius_x=6, sweep=False)
        self.add_line('e3-8', (32, 22), (29, 29))
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', closed=True)
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c3')
