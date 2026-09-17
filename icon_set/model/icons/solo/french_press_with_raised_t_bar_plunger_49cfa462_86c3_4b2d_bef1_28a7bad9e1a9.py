"""French Press Coffee Maker.

Plan: French press with raised T grip, central plunger, interior filter and side handle. Bounds (6,6)-(42,42). Tiny feet omitted.
Construction reference: Lucide coffee: vessel and handle; no useful exact French-press match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '49cfa462-86c3-4b2d-bef1-28a7bad9e1a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee cold press_49cfa462-86c3-4b2d-bef1-28a7bad9e1a9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'french-press-with-raised-t-bar-plunger'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('french', 'press', 'coffee', 'maker')

    def build(self):
        poly(self,'body',(6,16),(22,16),(34,16),(34,20),(34,32),(34,34),(34,42),(10,42),(10,32),(10,22),(6,16))
        poly(self,'grip',(14,6),(22,6),(30,6))
        poly(self,'rod',(22,6),(22,16),(22,32))
        poly(self,'filter',(10,32),(22,32),(34,32))
        path(self,'handle',(34,20),('A',8,7,True,(34,34)))
        contacts(self)
