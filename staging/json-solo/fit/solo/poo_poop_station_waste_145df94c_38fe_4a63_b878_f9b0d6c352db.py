"""Poo poop station waste (babies), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '145df94c-38fe-4a63-b878-f9b0d6c352db'
SOURCE_PATH = 'icons-json/babies/poo poop station waste_145df94c-38fe-4a63-b878-f9b0d6c352db.json'
AUTHOR = 'json_to_solo'

class PooPoopStationWaste(Solo48):
    icon_id = 'poo-poop-station-waste'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('poo', 'poop', 'station', 'waste', 'babies')

    def build(self):
        self.add_line('e0', (19, 18), (18, 16))
        self.add_line('e1', (18, 16), (18, 14))
        self.add_line('e2', (18, 14), (20, 11))
        self.add_line('e3', (27, 19), (26, 17))
        self.add_line('e4', (42, 42), (37, 42))
        self.add_line('e5', (11, 42), (6, 42))
        self.add_line('e6', (6, 42), (6, 34))
        self.add_line('e7', (19, 28), (28, 28))
        self.add_line('e8', (35, 22), (37, 14))
        self.add_arc('e9', (20, 11), (19, 6), radius_x=5, sweep=False)
        self.add_arc('e10', (26, 17), (28, 10), radius_x=6, sweep=False)
        self.add_arc('e11', (37, 42), (11, 42), radius_x=16, sweep=False)
        self.add_arc('e12-1', (6, 34), (9, 23), radius_x=33)
        self.add_arc('e12-2', (9, 23), (12, 22), radius_x=2)
        self.add_arc('e12-3', (12, 22), (19, 28), radius_x=9, sweep=False)
        self.add_arc('e13', (28, 28), (35, 22), radius_x=9, sweep=False)
        self.add_arc('e14-1', (37, 14), (39, 14), radius_x=2)
        self.add_arc('e14-2', (39, 14), (41, 20), radius_x=10)
        self.add_line('e14-3', (41, 20), (42, 41))
        self.add_line('e14-4', (42, 41), (42, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e9')
        self.add_contour('c1', 'e3', 'e10')
        self.add_contour('c2', 'e4', 'e11', 'e5', 'e6', 'e12-1', 'e12-2', 'e12-3', 'e7', 'e13', 'e8', 'e14-1', 'e14-2', 'e14-3', 'e14-4', closed=True)
