"""Delicata squash (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39f7021c-7064-4587-a19c-afa4eab4412a'
SOURCE_PATH = 'icons-json/food/delicata squash_39f7021c-7064-4587-a19c-afa4eab4412a.json'
AUTHOR = 'json_to_solo'

class DelicataSquashFood(Solo48):
    icon_id = 'delicata-squash-food'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('delicata', 'squash', 'food')

    def build(self):
        self.add_line('e0', (42, 6), (38, 10))
        self.add_arc('e1-1', (37, 11), (26, 21), radius_x=74, sweep=False)
        self.add_line('e1-2', (26, 21), (8, 40))
        self.add_line('e2-1', (8, 40), (14, 42))
        self.add_arc('e2-2', (14, 42), (34, 29), radius_x=28, sweep=False)
        self.add_arc('e2-3', (34, 29), (38, 10), radius_x=16, sweep=False)
        self.add_line('e3-1', (8, 40), (6, 35))
        self.add_arc('e3-2', (6, 35), (20, 13), radius_x=28)
        self.add_arc('e3-3', (20, 13), (38, 10), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3')
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
