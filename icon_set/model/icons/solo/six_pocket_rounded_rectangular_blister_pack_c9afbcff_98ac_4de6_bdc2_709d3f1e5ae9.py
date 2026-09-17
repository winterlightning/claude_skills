"""Pill Blister Pack.

Plan: Six-pocket blister card. Bounds (8,4)-(40,44); two columns and three rows share pitch. Pocket outlines reduced to six short pill-shaped raised marks to retain count with clear gaps.
Construction reference: Lucide pill: simple medicine silhouette; no useful exact blister match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c9afbcff-98ac-4de6-bdc2-709d3f1e5ae9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/ice tray_c9afbcff-98ac-4de6-bdc2-709d3f1e5ae9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'six-pocket-rounded-rectangular-blister-pack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('pill', 'blister', 'pack')

    def build(self):
        box(self,'card',8,4,40,44,6)
        for row in range(3):
         for col in range(2):
          line(self,f'pocket-{row}-{col}',(18+12*col,13+10*row),(18+12*col,15+10*row))
        contacts(self)
