"""Maps (maps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38385cd8-5a26-4e5a-9f9f-a365e79b13af'
SOURCE_PATH = 'icons-json/maps/maps_38385cd8-5a26-4e5a-9f9f-a365e79b13af.json'
AUTHOR = 'json_to_solo'

class MapsMaps(Solo48):
    icon_id = 'maps-maps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('maps',)

    def build(self):
        self.add_line('e0', (30, 6), (18, 14))
        self.add_line('e1', (30, 6), (30, 34))
        self.add_line('e2', (30, 6), (42, 13))
        self.add_line('e3', (42, 13), (42, 42))
        self.add_line('e4', (42, 42), (30, 34))
        self.add_line('e5', (18, 14), (6, 6))
        self.add_line('e6', (6, 6), (6, 34))
        self.add_line('e7', (6, 34), (18, 42))
        self.add_line('e8', (18, 14), (18, 42))
        self.add_line('e9', (18, 42), (30, 34))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
