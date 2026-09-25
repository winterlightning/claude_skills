"""Espresso Machine with Coffee Cup.

Plan: Espresso head, portafilter with projecting right handle, cup and tray. Bounds (6,6)-(42,42). Rear post, switch and short nozzle omitted for clarity.
Construction reference: Lucide coffee: rounded cup and open handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '213c71ae-a626-4bbc-875c-a8fa998c3a55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee machine_213c71ae-a626-4bbc-875c-a8fa998c3a55.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'espresso-machine-with-portafilter-and-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('espresso', 'machine', 'with', 'coffee', 'cup')

    def build(self):
        box(self,'head',6,6,42,14,2,xs=(22,30))
        poly(self,'frame',(6,12),(6,42),(22,42),(26,42),(42,42))
        poly(self,'filter',(22,14),(22,22),(30,22),(30,14))
        line(self,'filter-handle',(30,22),(42,22))
        path(self,'cup',(16,32),('L',(32,32)),('L',(32,36)),('A',6,6,True,(26,42)),('L',(22,42)),('A',6,6,True,(16,36)),('L',(16,32)),closed=True)
        path(self,'cup-handle',(32,32),('A',8,6,True,(40,38)))
        contacts(self)
