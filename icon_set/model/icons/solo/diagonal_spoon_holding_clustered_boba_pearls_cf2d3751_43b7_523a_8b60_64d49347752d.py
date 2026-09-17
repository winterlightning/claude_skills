"""Spoonful of Boba Pearls.

Plan: Diagonal spoon with three boba pearls on its bowl. Bounds (6,6)-(42,42). Solid pearl marks retain the food cue without crowded tiny holes; single-line handle keeps bowl spacious.
Construction reference: Lucide cherry: repeated rounded fruit; no exact spoonful match. Diagonal handle is deliberately asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'cf2d3751-43b7-523a-8b60-64d49347752d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/bubble tea on spoon_cf2d3751-43b7-523a-8b60-64d49347752d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'diagonal-spoon-holding-clustered-boba-pearls'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('spoonful', 'of', 'boba', 'pearls')

    def build(self):
        path(self,'bowl',(6,29),('L',(32,29)),('A',13,13,True,(19,42)),('A',13,13,True,(6,29)),closed=True)
        line(self,'handle',(32,29),(42,6))
        for i,(x,y) in enumerate(((9,20),(18,19),(27,17))):self.add_dot(f'pearl-{i}',(x,y))
        contacts(self)
