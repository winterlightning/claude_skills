"""Pathfinder merge (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5359e13c-d622-4650-8a34-9dcec3231c86'
SOURCE_PATH = 'icons-json/design/pathfinder merge_5359e13c-d622-4650-8a34-9dcec3231c86.json'
AUTHOR = 'json_to_solo'

class PathfinderMergeDesign(Solo48):
    icon_id = 'pathfinder-merge-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'merge', 'design')

    def build(self):
        self.add_line('e0', (16, 30), (6, 30))
        self.add_line('e1', (4, 28), (4, 10))
        self.add_line('e2', (6, 8), (28, 8))
        self.add_line('e3', (29, 10), (29, 18))
        self.add_line('e4', (29, 18), (42, 18))
        self.add_line('e5', (44, 20), (44, 38))
        self.add_line('e6', (42, 40), (19, 40))
        self.add_line('e7', (17, 38), (17, 30))
        self.add_bezier('e8', (6, 30), ((5.318, 29.731), (4.018, 29.28), (4.018, 28.387)), ((4.009, 28.328), (4, 28.059), (4, 28)))
        self.add_bezier('e9', (4, 10), ((4.555, 8.838), (4.7, 8.497), (6, 8)))
        self.add_bezier('e10', (28, 8), ((29.264, 8.488), (28.436, 8.88), (29, 10)))
        self.add_bezier('e11', (42, 18), ((42.655, 18.269), (43.5, 18.611), (43.855, 19.251)), ((43.955, 19.427), (43.918, 19.823), (44, 20)))
        self.add_bezier('e12', (44, 38), ((43.464, 39.255), (43.336, 39.478), (42, 40)))
        self.add_bezier('e13', (19, 40), ((18.918, 39.992), (19.282, 39.992), (19.2, 39.983)), ((18.036, 39.983), (17.591, 38.775), (17, 38)))
        self.add_bezier('e14', (17, 30), ((16.7, 30), (16.3, 30), (16, 30)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e4', 'e11', 'e5', 'e12', 'e6', 'e13', 'e7', 'e14', closed=True)
