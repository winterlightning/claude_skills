"""Classic Milk Bottle.

Plan: Broad-lipped milk bottle with mirrored shoulders and round base; bounds (10,4)-(38,44). Lip seam retained; no extra label.
Construction reference: Lucide milk: paired inward neck and outward shoulder arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5612c8eb-6383-491c-93b7-71057a5f1e8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/milk_5612c8eb-6383-491c-93b7-71057a5f1e8f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-milk-bottle-with-flared-mouth'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    aliases = ()
    keywords = ('classic', 'milk', 'bottle')

    def build(self):
        path(self,'lip',(16,12),('A',4,4,True,(16,4)),('L',(32,4)),('A',4,4,True,(32,12)),('L',(16,12)),closed=True)
        path(self,'body',(16,12),('L',(16,16)),('A',3,6,True,(13,22)),('A',3,6,False,(10,28)),('L',(10,38)),('A',6,6,False,(16,44)),('L',(32,44)),('A',6,6,False,(38,38)),('L',(38,28)),('A',3,6,False,(35,22)),('A',3,6,True,(32,16)),('L',(32,12)))
        contacts(self)
