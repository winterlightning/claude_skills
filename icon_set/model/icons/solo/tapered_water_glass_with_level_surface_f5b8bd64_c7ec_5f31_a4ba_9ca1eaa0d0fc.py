"""Drinking Glass with Water.

Plan: Tall tapered water glass, bounds (10,4)-(38,44). Symmetric sides and paired base radii; one level surface.
Construction reference: Lucide glass-water: taper, rounded base and water level.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f5b8bd64-c7ec-5f31-a4ba-9ca1eaa0d0fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/water glass_f5b8bd64-c7ec-5f31-a4ba-9ca1eaa0d0fc.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tapered-water-glass-with-level-surface'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('drinking', 'glass', 'with', 'water')

    def build(self):
        axis=24
        path(self,'glass',(axis-14,4),('L',(axis+14,4)),('L',(axis+12,22)),('L',(axis+10,40)),('A',4,4,True,(axis+6,44)),('L',(axis-6,44)),('A',4,4,True,(axis-10,40)),('L',(axis-12,22)),('L',(axis-14,4)),closed=True)
        line(self,'water',(12,22),(36,22))
        contacts(self)
