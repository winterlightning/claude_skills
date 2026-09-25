"""Independent 32px profile of spark.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4ad58635-e2af-414f-ab7d-37140c1f0e2d'
SOURCE_PATH = 'pictographic-primitives/symbol/spark_4ad58635-e2af-414f-ab7d-37140c1f0e2d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ad58635-e2af-414f-ab7d-37140c1f0e2d', 'pictographic-primitives/symbol/spark_4ad58635-e2af-414f-ab7d-37140c1f0e2d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/spark',)
SOLO_SOURCE_ICON_IDS = ('spark',)
REFERENCE_EXPORT_SHA256 = '50359e210f97ad0987d79e31bacfdac5300c71623432105ea64b16c519d06731'

class Drawing(Sub32):
    icon_id = 'spark-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (7, 14))
        self.add_arc('p1-r1-2', (7, 14), (14, 6), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (14, 6), (16, 2))
        self.add_line('p1-r1-4', (16, 2), (18, 6))
        self.add_arc('p1-r1-5', (18, 6), (26, 14), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (26, 14), (30, 16))
        self.add_line('p1-r1-7', (30, 16), (26, 18))
        self.add_arc('p1-r1-8', (26, 18), (18, 25), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('p1-r1-9', (18, 25), (16, 30))
        self.add_line('p1-r1-10', (16, 30), (14, 26))
        self.add_arc('p1-r1-11', (14, 26), (6, 18), radius_x=21, radius_y=21, large_arc=False, sweep=False)
        self.add_line('p1-r1-12', (6, 18), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
