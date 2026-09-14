"""Cellar (building), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c536474-4cfa-4c4a-bf71-7af160b27cb6'
SOURCE_PATH = 'icons-json/building/cellar_0c536474-4cfa-4c4a-bf71-7af160b27cb6.json'
AUTHOR = 'json_to_solo'

class CellarBuilding(Solo48):
    icon_id = 'cellar-building'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('cellar', 'building')

    def build(self):
        self.add_line('e0', (24, 6), (24, 42))
        self.add_line('e1', (42, 42), (42, 22))
        self.add_line('e2', (6, 22), (6, 42))
        self.add_line('e3', (6, 42), (42, 42))
        self.add_bezier('e4', (15, 26), ((15, 26.27), (15, 26.73), (15, 27)))
        self.add_bezier('e5', (31, 26), ((31, 26.27), (31, 26.73), (31, 27)))
        self.add_bezier('e6', (42, 22), ((42, 20.756), (41.558, 18.935), (41.174, 17.765)), ((38.85, 10.835), (31.691, 6.008), (24.425, 6.008)), ((24.352, 6.008), (24.286, 6), (24.213, 6)), ((24.139, 6), (24.074, 6), (24, 6)), ((23.722, 6), (23.452, 6.008), (23.174, 6.008)), ((16.145, 6.008), (9.363, 10.966), (6.892, 17.471)), ((6.434, 18.69), (6.008, 20.13), (6.008, 21.447)), ((6.008, 21.48), (6, 21.967), (6, 22)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e1', 'e6', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
