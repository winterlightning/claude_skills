"""Wooden Block Tower.

Plan: Alternating broad and narrow wooden blocks with one leaning piece to the right. Shared row heights and seams; reduce upright subdivisions. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4795457-fa78-561c-bd12-1e0cb66cf3e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/board game jenga_f4795457-fa78-561c-bd12-1e0cb66cf3e6.svg'
AUTHOR = 'gpt-6'

class WoodenBlockTower(Solo48):
    icon_id = 'wooden-block-tower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    aliases = ()
    keywords = ('wooden', 'block', 'tower')

    def build(self):
        self.add_polyline('tower',(6,6),(22,6),(22,14),(14,14),(14,26),(22,26),(22,34),(22,42),(14,42),(6,42),(6,34),(6,26),(6,14),closed=True)
        for n,a,b in [('top',(6,14),(14,14)),('middle',(6,26),(14,26)),('bottom',(6,34),(22,34)),('split',(14,34),(14,42))]:
         self.add_line(n,a,b);self.relate('connect','tower',n)
        self.relate('connect','bottom','split')
        self.add_polyline('leaning',(32,18),(40,16),(42,38),(34,40),closed=True)
