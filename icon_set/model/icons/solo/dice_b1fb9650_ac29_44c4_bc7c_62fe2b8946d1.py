"""Dice (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1fb9650-ac29-44c4-bc7c-62fe2b8946d1'
SOURCE_PATH = 'icons-json/entertainment/dice_b1fb9650-ac29-44c4-bc7c-62fe2b8946d1.json'
AUTHOR = 'json_to_solo'

class DiceB1fb9650(Solo48):
    icon_id = 'dice-b1fb9650'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (24, 24), (24, 24))
        self.add_line('sym-e1', (6, 24), (6, 11))
        self.add_arc('sym-e3', (6, 11), (11, 6), radius_x=5)
        self.add_line('sym-e5', (11, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (37, 6))
        self.add_arc('sym-e8', (37, 6), (42, 11), radius_x=5)
        self.add_line('sym-e10', (42, 11), (42, 24))
        self.add_line('sym-e11', (42, 24), (42, 37))
        self.add_arc('sym-e13', (42, 37), (37, 42), radius_x=5)
        self.add_line('sym-e15', (37, 42), (24, 42))
        self.add_line('sym-e16', (24, 42), (11, 42))
        self.add_arc('sym-e18', (11, 42), (6, 37), radius_x=5)
        self.add_line('sym-e20', (6, 37), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e20', closed=True)
