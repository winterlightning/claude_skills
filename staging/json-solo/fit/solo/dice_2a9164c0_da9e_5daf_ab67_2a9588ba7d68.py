"""Dice (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a9164c0-da9e-5daf-ab67-2a9588ba7d68'
SOURCE_PATH = 'icons-json/entertainment/dice_2a9164c0-da9e-5daf-ab67-2a9588ba7d68.json'
AUTHOR = 'json_to_solo'

class Dice2a9164c0(Solo48):
    icon_id = 'dice-2a9164c0'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')

    def build(self):
        self.add_arc('sym-e0', (20, 24), (28, 24), radius_x=4)
        self.add_arc('sym-e1', (28, 24), (20, 24), radius_x=4)
        self.add_line('sym-e3-1', (12, 6), (8, 7))
        self.add_line('sym-e3-2', (8, 7), (6, 11))
        self.add_line('sym-e4', (6, 11), (6, 12))
        self.add_line('sym-e5', (6, 12), (6, 13))
        self.add_line('sym-e6', (6, 13), (6, 14))
        self.add_line('sym-e8', (6, 14), (6, 35))
        self.add_line('sym-e9', (6, 35), (6, 36))
        self.add_line('sym-e10-1', (6, 36), (7, 40))
        self.add_line('sym-e10-2', (7, 40), (10, 42))
        self.add_line('sym-e11', (10, 42), (12, 42))
        self.add_arc('sym-e12', (12, 42), (13, 42), radius_x=1)
        self.add_line('sym-e14', (13, 42), (24, 42))
        self.add_line('sym-e15', (24, 42), (35, 42))
        self.add_line('sym-e17', (35, 42), (36, 42))
        self.add_line('sym-e18', (36, 42), (38, 42))
        self.add_line('sym-e19-1', (38, 42), (41, 40))
        self.add_line('sym-e19-2', (41, 40), (42, 36))
        self.add_arc('sym-e20', (42, 36), (42, 35), radius_x=37)
        self.add_line('sym-e21', (42, 35), (42, 14))
        self.add_line('sym-e23', (42, 14), (42, 13))
        self.add_line('sym-e24', (42, 13), (42, 12))
        self.add_line('sym-e25', (42, 12), (42, 11))
        self.add_arc('sym-e26-1', (42, 11), (40, 7), radius_x=6, sweep=False)
        self.add_line('sym-e26-2', (40, 7), (36, 6))
        self.add_line('sym-e28', (36, 6), (24, 6))
        self.add_line('sym-e29', (24, 6), (12, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e19-1', 'sym-e19-2', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26-1', 'sym-e26-2', 'sym-e28', 'sym-e29', closed=True)
