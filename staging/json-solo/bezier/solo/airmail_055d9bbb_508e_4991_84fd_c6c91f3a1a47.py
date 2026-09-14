"""Airmail (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '055d9bbb-508e-4991-84fd-c6c91f3a1a47'
SOURCE_PATH = 'icons-json/_uncategorized_01/airmail_055d9bbb-508e-4991-84fd-c6c91f3a1a47.json'
AUTHOR = 'json_to_solo'

class AirmailUncategorized01(Solo48):
    icon_id = 'airmail-uncategorized-01'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('airmail', '_uncategorized_01')

    def build(self):
        self.add_line('sym-e0', (44, 39), (41, 40))
        self.add_line('sym-e1', (41, 40), (7, 40))
        self.add_line('sym-e2', (7, 40), (4, 39))
        self.add_bezier('sym-e3', (4, 39), ((4, 38.33), (4, 37.67), (4, 37)))
        self.add_line('sym-e4', (4, 37), (4, 10))
        self.add_line('sym-e5', (4, 10), (19, 24))
        self.add_line('sym-e6', (19, 24), (23, 27))
        self.add_bezier('sym-e7', (23, 27), ((23.373, 27.31), (23.732, 27.001), (24, 27)))
        self.add_bezier('sym-e8', (24, 27), ((24.268, 27.001), (24.627, 27.31), (25, 27)))
        self.add_line('sym-e9', (25, 27), (29, 24))
        self.add_line('sym-e10', (29, 24), (44, 10))
        self.add_line('sym-e11', (44, 10), (44, 37))
        self.add_bezier('sym-e12', (44, 37), ((44, 37.67), (44, 38.33), (44, 39)))
        self.add_line('sym-e13', (44, 39), (29, 24))
        self.add_line('sym-e14', (4, 10), (6, 8))
        self.add_bezier('sym-e15', (6, 8), ((6.3, 8), (6.7, 8), (7, 8)))
        self.add_line('sym-e16', (7, 8), (24, 8))
        self.add_line('sym-e17', (24, 8), (41, 8))
        self.add_bezier('sym-e18', (41, 8), ((41.3, 8), (41.7, 8), (42, 8)))
        self.add_line('sym-e19', (42, 8), (44, 10))
        self.add_line('sym-e20', (19, 24), (4, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c2', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
