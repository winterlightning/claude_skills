"""Iced Coffee Glass with Straw.

Plan: Iced drink with right-bent straw and two complete ice cubes. Bounds (4,8)-(44,40). Glass broadened and cubes arranged side by side; wave and taper omitted to retain both clear cube outlines.
Construction reference: Lucide cup-soda: glass and bent straw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '4daf9729-9636-5534-8214-749f5664cd5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee coldbrew_4daf9729-9636-5534-8214-749f5664cd5b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'iced-drink-with-two-cubes-and-bent-straw'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('iced', 'coffee', 'glass', 'with', 'straw')

    def build(self):
        poly(self,'glass',(4,16),(28,16),(44,16),(44,40),(4,40),(4,16))
        poly(self,'straw',(28,16),(32,8),(44,8))
        for i,x in enumerate((12,28)):
         poly(self,f'ice-{i}',(x,24),(x+8,24),(x+8,32),(x,32),(x,24))
        contacts(self)
