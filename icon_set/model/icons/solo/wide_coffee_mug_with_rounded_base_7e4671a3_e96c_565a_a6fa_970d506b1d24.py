"""Classic Ceramic Coffee Mug.

Plan: Wide ceramic cup with deep curved base and attached handle; bounds (4,10)-(44,38).
Construction reference: Lucide coffee: coherent round base and open handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7e4671a3-e96c-565a-a6fa-970d506b1d24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee cup_7e4671a3-e96c-565a-a6fa-970d506b1d24.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'wide-coffee-mug-with-rounded-base'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    categories = ('drinks', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('classic', 'ceramic', 'coffee', 'mug')

    def build(self):
        path(self,'body',(4,10),('L',(34,10)),('L',(34,14)),('L',(34,30)),('A',8,8,True,(26,38)),('L',(12,38)),('A',8,8,True,(4,30)),('L',(4,10)),closed=True)
        path(self,'handle',(34,14),('L',(36,14)),('A',8,8,True,(36,30)),('L',(34,30)))
        contacts(self)
