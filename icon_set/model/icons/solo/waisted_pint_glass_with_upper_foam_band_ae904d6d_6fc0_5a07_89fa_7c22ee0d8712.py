"""Pint of Draft Beer.

Plan: Waisted pint glass with broad upper foam band. Bounds (10,4)-(38,44); mirrored side arcs and rounded base. Reflection omitted as secondary detail.
Construction reference: Lucide glass-water: open glass silhouette and level band.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ae904d6d-6fc0-5a07-89fa-7c22ee0d8712'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/beer glass_ae904d6d-6fc0-5a07-89fa-7c22ee0d8712.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'waisted-pint-glass-with-upper-foam-band'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('pint', 'of', 'draft', 'beer')

    def build(self):
        path(self,'glass',(10,4),('L',(38,4)),('L',(38,14)),('A',6,18,False,(32,32)),('L',(32,40)),('A',4,4,True,(28,44)),('L',(20,44)),('A',4,4,True,(16,40)),('L',(16,32)),('A',6,18,False,(10,14)),('L',(10,4)),closed=True)
        line(self,'foam-band',(10,14),(38,14))
        contacts(self)
