"""Synchronize refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0553293-203d-4c9b-9583-f6ead215b9d7'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow_a0553293-203d-4c9b-9583-f6ead215b9d7.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow(Solo48):
    icon_id = 'synchronize-refresh-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (39, 20), (40, 25))
        self.add_line('e1', (34, 21), (40, 25))
        self.add_line('e2', (44, 19), (40, 25))
        self.add_bezier('e3', (24, 40), ((23.5, 40), (23.009, 39.983), (22.509, 39.983)), ((22.318, 39.983), (22.127, 39.983), (21.936, 39.983)), ((21.745, 39.983), (21.545, 40), (21.355, 40)), ((21.264, 40), (21.173, 39.992), (21.082, 39.992)), ((12.255, 39.992), (4.009, 32.463), (4.009, 24.286)), ((4.009, 24.203), (4, 24.129), (4, 24.046)), ((4, 24.045), (4, 24.043), (4, 24.042)), ((4, 23.874), (4.009, 23.705), (4.009, 23.537)), ((4.009, 16.623), (9.718, 10.619), (16.673, 8.724)), ((18.1, 8.337), (19.636, 8.017), (21.136, 8.017)), ((21.36, 8.017), (21.575, 8), (21.798, 8)), ((21.802, 8), (21.806, 8), (21.809, 8)), ((22.1, 8), (22.382, 8.017), (22.673, 8.017)), ((28.955, 8.017), (34.973, 11.731), (38.045, 16.657)), ((38.618, 17.592), (38.809, 18.922), (39, 20)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
