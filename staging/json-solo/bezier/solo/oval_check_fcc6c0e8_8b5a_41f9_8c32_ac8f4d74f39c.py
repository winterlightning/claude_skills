"""Oval check (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c'
SOURCE_PATH = 'icons-json/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.json'
AUTHOR = 'json_to_solo'

class OvalCheckState(Solo48):
    icon_id = 'oval-check-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('oval', 'check', 'state')

    def build(self):
        self.add_line('e0', (33, 17), (21, 31))
        self.add_line('e1', (21, 31), (15, 23))
        self.add_line('e2', (33, 8), (15, 8))
        self.add_line('e3', (15, 40), (33, 40))
        self.add_bezier('e4', (15, 8), ((14.182, 8), (13.227, 8.382), (12.464, 8.738)), ((7.945, 10.806), (4.009, 16.775), (4.009, 23.471)), ((4.009, 23.592), (4, 23.713), (4, 23.834)), ((4, 23.836), (4, 23.838), (4, 23.84)), ((4, 24.074), (4.009, 24.295), (4.009, 24.529)), ((4.009, 31.705), (9.555, 40), (15, 40)))
        self.add_bezier('e5', (33, 40), ((33.1, 39.988), (33.291, 39.988), (33.391, 39.975)), ((34.164, 39.975), (35.045, 39.569), (35.773, 39.237)), ((40.282, 37.169), (43.991, 30.978), (43.991, 24.406)), ((43.991, 24.297), (44, 24.188), (44, 24.079)), ((44, 24.077), (44, 24.076), (44, 24.074)), ((44, 23.84), (43.991, 23.606), (43.991, 23.372)), ((43.991, 16.677), (40.191, 10.745), (35.645, 8.726)), ((34.955, 8.418), (34.109, 8.025), (33.373, 8.025)), ((33.282, 8.012), (33.091, 8.012), (33, 8)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e4', 'e3', 'e5', closed=True)
