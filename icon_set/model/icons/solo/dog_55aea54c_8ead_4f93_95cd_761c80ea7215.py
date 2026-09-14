"""Dog (pets), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55aea54c-8ead-4f93-95cd-761c80ea7215'
SOURCE_PATH = 'icons-json/pets/dog_55aea54c-8ead-4f93-95cd-761c80ea7215.json'
AUTHOR = 'json_to_solo'

class Dog(Solo48):
    icon_id = 'dog'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('dog', 'pets')

    def build(self):
        self.add_line('e0', (6, 35), (9, 27))
        self.add_line('e1', (17, 11), (21, 6))
        self.add_line('e2', (28, 17), (35, 18))
        self.add_line('e3', (25, 33), (23, 42))
        self.add_line('e4', (9, 27), (17, 11))
        self.add_arc('e5-1', (21, 6), (24, 15), radius_x=55, sweep=False)
        self.add_arc('e5-2', (24, 15), (28, 17), radius_x=4, sweep=False)
        self.add_arc('e6-1', (35, 18), (42, 24), radius_x=7)
        self.add_line('e6-2', (42, 24), (41, 28))
        self.add_arc('e6-3', (41, 28), (38, 31), radius_x=8)
        self.add_arc('e6-4', (38, 31), (25, 33), radius_x=33)
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e3')
