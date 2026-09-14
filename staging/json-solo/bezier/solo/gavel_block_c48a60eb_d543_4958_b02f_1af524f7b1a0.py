"""Gavel block (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c48a60eb-d543-4958-b02f-1af524f7b1a0'
SOURCE_PATH = 'icons-json/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.json'
AUTHOR = 'json_to_solo'

class GavelBlockState(Solo48):
    icon_id = 'gavel-block-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('gavel', 'block', 'state')

    def build(self):
        self.add_line('e0', (5, 8), (43, 8))
        self.add_line('e1', (44, 10), (44, 38))
        self.add_line('e2', (43, 40), (5, 40))
        self.add_line('e3', (4, 38), (4, 10))
        self.add_bezier('e4', (43, 8), ((43.064, 8), (43.209, 8.023), (43.273, 8.023)), ((43.591, 8.023), (43.982, 9.029), (43.982, 9.829)), ((43.991, 9.966), (43.991, 9.84), (44, 10)))
        self.add_bezier('e5', (44, 38), ((43.991, 38.16), (43.991, 38.034), (43.982, 38.171)), ((43.982, 38.971), (43.591, 39.977), (43.273, 39.977)), ((43.209, 39.977), (43.064, 40), (43, 40)))
        self.add_bezier('e6', (5, 40), ((4.936, 40), (4.791, 39.977), (4.727, 39.977)), ((4.409, 39.977), (4.018, 38.971), (4.018, 38.171)), ((4.009, 38.034), (4.009, 38.16), (4, 38)))
        self.add_bezier('e7', (4, 10), ((4.009, 9.84), (4.009, 9.966), (4.018, 9.829)), ((4.018, 9.029), (4.409, 8.023), (4.727, 8.023)), ((4.791, 8.023), (4.936, 8), (5, 8)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', closed=True)
