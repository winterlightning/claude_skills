"""Alcove (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c5e171c-ba31-4513-a36c-dbb30aad9abc'
SOURCE_PATH = 'icons-json/_uncategorized_01/alcove_5c5e171c-ba31-4513-a36c-dbb30aad9abc.json'
AUTHOR = 'json_to_solo'

class Alcove(Solo48):
    icon_id = 'alcove'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('alcove', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (16, 35), (32, 35))
        self.add_line('e1', (16, 35), (16, 20))
        self.add_line('e2', (32, 20), (32, 35))
        self.add_line('e3', (38, 41), (40, 44))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_line('e5', (8, 44), (8, 39))
        self.add_line('e6', (8, 39), (8, 19))
        self.add_line('e7', (40, 19), (40, 44))
        self.add_arc('e8', (16, 35), (8, 44), radius_x=21, sweep=False)
        self.add_arc('e9-1', (16, 20), (22, 13), radius_x=8)
        self.add_arc('e9-2', (22, 13), (32, 20), radius_x=8)
        self.add_arc('e10', (32, 35), (38, 41), radius_x=16)
        self.add_arc('e11-1', (8, 19), (24, 4), radius_x=17)
        self.add_line('e11-2', (24, 4), (32, 6))
        self.add_arc('e11-3', (32, 6), (40, 19), radius_x=16)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e1', 'e9-1', 'e9-2', 'e2')
        self.add_contour('c3', 'e10', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', 'e11-1', 'e11-2', 'e11-3', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
