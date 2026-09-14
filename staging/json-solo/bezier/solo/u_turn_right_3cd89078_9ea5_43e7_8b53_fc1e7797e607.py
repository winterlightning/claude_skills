"""U turn right (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cd89078-9ea5-43e7-8b53-fc1e7797e607'
SOURCE_PATH = 'icons-json/transportation/u turn right_3cd89078-9ea5-43e7-8b53-fc1e7797e607.json'
AUTHOR = 'json_to_solo'

class UTurnRightTransportation(Solo48):
    icon_id = 'u-turn-right-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('u', 'turn', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (6, 42), (6, 22))
        self.add_line('e1', (35, 27), (35, 34))
        self.add_line('e2', (35, 34), (42, 25))
        self.add_line('e3', (35, 34), (24, 24))
        self.add_bezier('e4', (6, 22), ((6, 21.787), (6, 21.938), (6, 21.725)), ((6, 19.778), (6.164, 17.176), (6.802, 15.335)), ((8.602, 10.075), (14.026, 6.016), (19.655, 6.016)), ((19.841, 6.016), (20.034, 6), (20.227, 6)), ((20.23, 6), (20.233, 6), (20.236, 6)), ((20.498, 6), (20.76, 6.016), (21.022, 6.016)), ((26.97, 6.016), (32.599, 10.508), (34.105, 16.195)), ((34.98, 19.549), (35, 23.539), (35, 27)))
        self.add_contour('c0', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
