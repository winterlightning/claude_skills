"""Spark (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ad58635-e2af-414f-ab7d-37140c1f0e2d'
SOURCE_PATH = 'icons-json/symbol/spark_4ad58635-e2af-414f-ab7d-37140c1f0e2d.json'
AUTHOR = 'json_to_solo'

class SparkSymbol(Solo48):
    icon_id = 'spark-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('spark', 'symbol')

    def build(self):
        self.add_line('e0', (6, 24), (12, 22))
        self.add_line('e1', (22, 11), (24, 6))
        self.add_line('e2', (24, 6), (26, 11))
        self.add_line('e3', (37, 22), (42, 24))
        self.add_line('e4', (42, 24), (37, 26))
        self.add_line('e5', (26, 36), (24, 42))
        self.add_line('e6', (24, 42), (22, 37))
        self.add_line('e7', (11, 26), (6, 24))
        self.add_bezier('e8', (12, 22), ((16.148, 20.225), (20.028, 14.944), (22, 11)))
        self.add_bezier('e9', (26, 11), ((28.225, 15.451), (32.549, 19.775), (37, 22)))
        self.add_bezier('e10', (37, 26), ((33.318, 27.841), (27.653, 32.146), (26, 36)))
        self.add_bezier('e11', (22, 37), ((21.648, 35.953), (21.341, 35.185), (20.727, 34.293)), ((18.935, 31.691), (16.775, 29.392), (14.182, 27.567)), ((13.159, 26.847), (12.203, 26.401), (11, 26)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e2', 'e9', 'e3', 'e4', 'e10', 'e5', 'e6', 'e11', 'e7', closed=True)
