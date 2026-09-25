"""Takeaway Coffee Cup.

Plan: Tall takeaway coffee cup with projecting rim and raised trapezoid lid. Bounds (8,4)-(40,44); mirrored taper and base corners.
Construction reference: Lucide cup-soda: tapered body and extended rim; stepped lid from reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a20b9c78-c072-503e-895f-41776bb0f49d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee to go_a20b9c78-c072-503e-895f-41776bb0f49d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'takeaway-coffee-cup-with-stepped-lid'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('takeaway', 'coffee', 'cup')

    def build(self):
        poly(self,'lid',(8,12),(12,4),(36,4),(40,12),(8,12))
        path(self,'cup',(10,12),('L',(14,40)),('A',4,4,False,(18,44)),('L',(30,44)),('A',4,4,False,(34,40)),('L',(38,12)))
        contacts(self)
