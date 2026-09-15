"""Dice (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2a9164c0-da9e-5daf-ab67-2a9588ba7d68'
SOURCE_PATH = 'pictographic-primitives/entertainment/dice_2a9164c0-da9e-5daf-ab67-2a9588ba7d68.svg'
AUTHOR = 'gpt-6'

class Dice(Solo48):
    icon_id = 'dice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')

    def build(self):
        self.add_arc('sym-e0', (20, 24), (28, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (28, 24), (20, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e3-1', (12, 6), (8, 7))
        self.add_line('sym-e3-2', (8, 7), (6, 11))
        self.add_line('sym-e4', (6, 11), (6, 36))
        self.add_line('sym-e10-1', (6, 36), (7, 40))
        self.add_line('sym-e10-2', (7, 40), (10, 42))
        self.add_line('sym-e11', (10, 42), (12, 42))
        self.add_arc('sym-e12', (12, 42), (13, 42), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e14', (13, 42), (38, 42))
        self.add_line('sym-e19-1', (38, 42), (41, 40))
        self.add_line('sym-e19-2', (41, 40), (42, 36))
        self.add_arc('sym-e20', (42, 36), (42, 35), radius_x=37, radius_y=37, large_arc=False, sweep=True)
        self.add_line('sym-e21', (42, 35), (42, 11))
        self.add_arc('sym-e26-1', (42, 11), (40, 7), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e26-2', (40, 7), (36, 6))
        self.add_line('sym-e28', (36, 6), (12, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e19-1', 'sym-e19-2', 'sym-e20', 'sym-e21', 'sym-e26-1', 'sym-e26-2', 'sym-e28', closed=True)
