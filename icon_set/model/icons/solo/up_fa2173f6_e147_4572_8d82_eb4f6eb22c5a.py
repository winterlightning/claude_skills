"""Up (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa2173f6-e147-4572-8d82-eb4f6eb22c5a'
SOURCE_PATH = 'icons-json/arrows/up_fa2173f6-e147-4572-8d82-eb4f6eb22c5a.json'
AUTHOR = 'json_to_solo'

class Up(Solo48):
    icon_id = 'up'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('up', 'arrows')

    def build(self):
        self.add_line('e0', (33, 10), (38, 6))
        self.add_line('e1', (37, 12), (38, 6))
        self.add_line('e2', (42, 11), (38, 6))
        self.add_line('e3', (32, 11), (33, 10))
        self.add_arc('e4-1', (6, 42), (19, 38), radius_x=39, sweep=False)
        self.add_arc('e4-2', (19, 38), (37, 12), radius_x=35, sweep=False)
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
