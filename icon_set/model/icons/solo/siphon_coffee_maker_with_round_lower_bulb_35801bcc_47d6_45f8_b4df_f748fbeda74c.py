"""Siphon Coffee Maker.

Plan: Upper cylinder and round lower bulb with right stand and burner base. Bounds (8,4)-(40,44); small liquid levels omitted and burner box reduced to a broad base to preserve a truly round bulb.
Construction reference: Lucide coffee and laboratory flask principles: coherent vessels and supporting stem.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '35801bcc-47d6-45f8-b4df-f748fbeda74c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee syphon_35801bcc-47d6-45f8-b4df-f748fbeda74c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'siphon-coffee-maker-with-round-lower-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('siphon', 'coffee', 'maker')

    def build(self):
        path(self,'upper',(8,4),('L',(28,4)),('L',(28,12)),('A',10,6,True,(18,18)),('A',10,6,True,(8,12)),('L',(8,4)),closed=True)
        path(self,'bulb',(18,18),('A',8,8,True,(26,26)),('A',8,8,True,(18,34)),('A',8,8,True,(10,26)),('A',8,8,True,(18,18)),closed=True)
        path(self,'stand',(18,18),('L',(34,18)),('A',6,6,True,(40,24)),('L',(40,44)),('L',(8,44)))
        contacts(self)
