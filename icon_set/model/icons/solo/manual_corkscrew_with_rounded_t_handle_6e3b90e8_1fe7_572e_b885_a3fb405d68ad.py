"""Simple Manual Wine Corkscrew.

Plan: Horizontal capsule grip and descending helical wire. Bounds (6,6)-(42,42). Shared arc radii build a smooth repeated corkscrew; grip pinch removed.
Construction reference: No useful local exact corkscrew match; geometric capsule and repeating arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '6e3b90e8-1fe7-572e-b885-a3fb405d68ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/wine opener_6e3b90e8-1fe7-572e-b885-a3fb405d68ad.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'manual-corkscrew-with-rounded-t-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('simple', 'manual', 'wine', 'corkscrew')

    def build(self):
        box(self,'grip',6,6,42,16,5,xs=(24,))
        path(self,'wire',(24,16),('L',(24,22)),('A',4,3,True,(20,25)),('A',4,3,False,(20,31)),('L',(28,35)),('A',4,3,True,(28,41)),('L',(26,42)))
        contacts(self)
