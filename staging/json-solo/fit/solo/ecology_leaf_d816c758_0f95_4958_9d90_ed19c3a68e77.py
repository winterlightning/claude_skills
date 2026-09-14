"""Ecology leaf (ecology), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd816c758-0f95-4958-9d90-ed19c3a68e77'
SOURCE_PATH = 'icons-json/ecology/ecology leaf_d816c758-0f95-4958-9d90-ed19c3a68e77.json'
AUTHOR = 'json_to_solo'

class EcologyLeafEcology(Solo48):
    icon_id = 'ecology-leaf-ecology'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('ecology', 'leaf')

    def build(self):
        self.add_line('e0', (4, 37), (8, 34))
        self.add_line('e1', (34, 12), (23, 12))
        self.add_arc('e2', (27, 22), (8, 34), radius_x=61, sweep=False)
        self.add_arc('e3-1', (23, 12), (6, 29), radius_x=19, sweep=False)
        self.add_arc('e3-2', (6, 29), (12, 38), radius_x=11, sweep=False)
        self.add_line('e3-3', (12, 38), (20, 40))
        self.add_arc('e3-4', (20, 40), (35, 34), radius_x=24, sweep=False)
        self.add_arc('e3-5', (35, 34), (42, 25), radius_x=25, sweep=False)
        self.add_line('e3-6', (42, 25), (44, 14))
        self.add_arc('e3-7', (44, 14), (44, 8), radius_x=47)
        self.add_line('e3-8', (44, 8), (42, 9))
        self.add_arc('e3-9', (42, 9), (34, 12), radius_x=15)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
