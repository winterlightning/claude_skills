"""Takeaway Drink Cup with Straw.

Plan: Straight central straw above extended lid and upper cup band. Bounds (8,4)-(40,44); symmetric taper with rounded base.
Construction reference: Lucide cup-soda: tapered cup and straw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '13dcc618-4810-41aa-a6d9-2196457533c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/bubble tea_13dcc618-4810-41aa-a6d9-2196457533c6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'takeaway-cup-with-straight-central-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('takeaway', 'drink', 'cup', 'with', 'straw')

    def build(self):
        line(self,'lid',(8,14),(40,14))
        line(self,'straw',(24,4),(24,14))
        path(self,'cup',(10,14),('L',(14,40)),('A',4,4,False,(18,44)),('L',(30,44)),('A',4,4,False,(34,40)),('L',(38,14)))
        line(self,'band',(11,22),(37,22))
        contacts(self)
