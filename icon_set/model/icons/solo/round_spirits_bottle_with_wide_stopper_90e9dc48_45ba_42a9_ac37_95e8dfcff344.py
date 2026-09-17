"""Glass Spirits Bottle.

Plan: Round spirits bottle with broad stopper, narrow neck and liquid line. Bounds (8,4)-(40,44); mirrored shoulders and rounded base.
Construction reference: Lucide bottle-wine and milk: paired neck-to-shoulder transitions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '90e9dc48-45ba-42a9-ac37-95e8dfcff344'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/spirits_90e9dc48-45ba-42a9-ac37-95e8dfcff344.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'round-spirits-bottle-with-wide-stopper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('glass', 'spirits', 'bottle')

    def build(self):
        box(self,'stopper',14,4,34,12,4)
        path(self,'body',(18,12),('L',(18,16)),('A',5,6,True,(13,22)),('A',5,6,False,(8,28)),('L',(8,32)),('A',8,12,False,(16,44)),('L',(32,44)),('A',8,12,False,(40,32)),('L',(40,28)),('A',5,6,False,(35,22)),('A',5,6,True,(30,16)),('L',(30,12)))
        line(self,'liquid',(8,32),(40,32))
        contacts(self)
