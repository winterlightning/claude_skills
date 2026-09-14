"""Angle (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02d7493f-77df-4e48-9a18-f7bb4fd11a95'
SOURCE_PATH = 'icons-json/_uncategorized_03/angle_02d7493f-77df-4e48-9a18-f7bb4fd11a95.json'
AUTHOR = 'json_to_solo'

class AngleUncategorized03(Solo48):
    icon_id = 'angle-uncategorized-03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angle', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (6, 31), (6, 42))
        self.add_line('e1', (6, 42), (17, 42))
        self.add_line('e2', (6, 31), (6, 6))
        self.add_line('e3', (6, 6), (42, 42))
        self.add_line('e4', (42, 42), (17, 42))
        self.add_arc('e5', (6, 31), (17, 42), radius_x=10)
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
