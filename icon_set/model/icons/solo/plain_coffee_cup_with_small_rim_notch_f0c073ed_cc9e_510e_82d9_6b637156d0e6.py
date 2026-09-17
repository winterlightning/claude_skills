"""Simple Coffee Cup.

Plan: Plain deep coffee cup with raised rim notch and right handle. Bounds (4,10)-(44,38); broad rounded base.
Construction reference: Lucide coffee: coherent base and attached curved handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f0c073ed-cc9e-510e-82d9-6b637156d0e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee mug_f0c073ed-cc9e-510e-82d9-6b637156d0e6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'plain-coffee-cup-with-small-rim-notch'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('simple', 'coffee', 'cup')

    def build(self):
        path(self,'cup',(4,12),('L',(24,12)),('L',(26,10)),('L',(32,10)),('L',(32,14)),('L',(32,30)),('A',8,8,True,(24,38)),('L',(12,38)),('A',8,8,True,(4,30)),('L',(4,12)),closed=True)
        path(self,'handle',(32,14),('A',12,8,True,(32,30)))
        contacts(self)
