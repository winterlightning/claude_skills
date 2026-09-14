"""Spark (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e8', (12, 22), (22, 11), radius_x=24, sweep=False)
        self.add_arc('e9', (26, 11), (37, 22), radius_x=25, sweep=False)
        self.add_arc('e10', (37, 26), (26, 36), radius_x=26, sweep=False)
        self.add_arc('e11', (22, 37), (11, 26), radius_x=27, sweep=False)
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e2', 'e9', 'e3', 'e4', 'e10', 'e5', 'e6', 'e11', 'e7', closed=True)
