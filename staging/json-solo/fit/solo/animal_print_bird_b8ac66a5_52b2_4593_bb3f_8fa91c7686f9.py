"""Animal print bird (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8ac66a5-52b2-4593-bb3f-8fa91c7686f9'
SOURCE_PATH = 'icons-json/_uncategorized_03/animal print bird_b8ac66a5-52b2-4593-bb3f-8fa91c7686f9.json'
AUTHOR = 'json_to_solo'

class AnimalPrintBirdUncategorized(Solo48):
    icon_id = 'animal-print-bird-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('animal', 'print', 'bird', '_uncategorized')

    def build(self):
        self.add_arc('e0-1', (12, 7), (6, 19), radius_x=18, sweep=False)
        self.add_line('e0-2', (6, 19), (8, 25))
        self.add_arc('e0-3', (8, 25), (9, 26), radius_x=6, sweep=False)
        self.add_arc('e0-4', (9, 26), (18, 25), radius_x=7, sweep=False)
        self.add_arc('e0-5', (18, 25), (13, 6), radius_x=15, sweep=False)
        self.add_line('e0-6', (13, 6), (12, 7))
        self.add_arc('e1-1', (35, 22), (29, 38), radius_x=14, sweep=False)
        self.add_arc('e1-2', (29, 38), (35, 42), radius_x=7, sweep=False)
        self.add_line('e1-3', (35, 42), (40, 40))
        self.add_line('e1-4', (40, 40), (42, 34))
        self.add_arc('e1-5', (42, 34), (39, 25), radius_x=15, sweep=False)
        self.add_arc('e1-6', (39, 25), (35, 21), radius_x=21, sweep=False)
        self.add_line('e1-7', (35, 21), (35, 22))
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', closed=True)
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', closed=True)
