"""Drinking Glass with Water.

Plan: Tall tapered water glass, bounds (10,4)-(38,44). Symmetric sides and paired base radii; one broad wave.
Construction reference: Lucide glass-water: taper, rounded base and water level.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9def73af-696c-5347-8021-04068caadf39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/water glass_9def73af-696c-5347-8021-04068caadf39.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tapered-water-glass-with-wavy-surface'
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
        path(self,'water',(12,22),('A',6,2,True,(24,22)),('A',6,2,False,(36,22)))
        contacts(self)
