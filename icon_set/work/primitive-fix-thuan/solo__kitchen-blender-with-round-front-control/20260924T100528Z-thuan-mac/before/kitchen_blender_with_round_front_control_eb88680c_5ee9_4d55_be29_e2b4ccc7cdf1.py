"""Electric Kitchen Blender.

Plan: Tapered blender jug, open handle and flared motor base with circular control. Bounds (8,4)-(40,44). Short feet omitted.
Construction reference: Lucide blender: jug/base proportions, control and open handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'eb88680c-5ee9-4d55-be29-e2b4ccc7cdf1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/vitamix_eb88680c-5ee9-4d55-be29-e2b4ccc7cdf1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'kitchen-blender-with-round-front-control'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('electric', 'kitchen', 'blender')

    def build(self):
        poly(self,'jug',(8,4),(32,4),(30,22),(14,22),(8,4))
        poly(self,'base',(14,22),(30,22),(38,44),(10,44),(14,22))
        path(self,'handle',(32,4),('A',8,10,True,(40,14)),('L',(40,20)))
        self.add_dot('control',(24,34))
        contacts(self)
