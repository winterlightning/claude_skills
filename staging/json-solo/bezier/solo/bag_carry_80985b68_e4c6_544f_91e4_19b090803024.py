"""Batch-07/bag carry (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80985b68-e4c6-544f-91e4-19b090803024'
SOURCE_PATH = 'icons-json/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.json'
AUTHOR = 'json_to_solo'

class Batch07BagCarry(Solo48):
    icon_id = 'batch-07-bag-carry'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'bag', 'carry', 'accessories')

    def build(self):
        self.add_line('e0', (37, 44), (12, 44))
        self.add_line('e1', (8, 40), (10, 13))
        self.add_line('e2', (10, 13), (38, 13))
        self.add_line('e3', (38, 13), (40, 37))
        self.add_bezier('e4', (32, 13), ((31.882, 11.791), (32.244, 10.536), (31.798, 9.391)), ((30.585, 6.3), (27.461, 4.018), (24.337, 4.018)), ((24.261, 4.009), (24.194, 4.009), (24.118, 4)), ((24.117, 4), (24.116, 4), (24.115, 4)), ((24.048, 4), (23.974, 4.009), (23.907, 4.009)), ((20.783, 4.009), (17.718, 6.082), (16.792, 9.373)), ((16.472, 10.536), (16.093, 11.809), (16, 13)))
        self.add_bezier('e5', (40, 37), ((40, 38.373), (39.992, 39.464), (39.992, 40.836)), ((39.992, 42.564), (38.474, 44), (37, 44)))
        self.add_bezier('e6', (12, 44), ((11.874, 43.991), (11.966, 43.991), (11.84, 43.982)), ((10.265, 43.982), (8.017, 42.473), (8.017, 40.591)), ((8.008, 40.518), (8.008, 40.073), (8, 40)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5', 'e0', 'e6', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
