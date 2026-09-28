"""Iced Coffee Glass with Straw.

Plan: Iced drink with right-bent straw and two complete ice cubes. Bounds (4,8)-(44,40). Glass broadened and cubes arranged side by side; wave and taper omitted to retain both clear cube outlines.
Construction reference: Lucide cup-soda: glass and bent straw.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '4daf9729-9636-5534-8214-749f5664cd5b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__iced-drink-with-two-cubes-and-bent-straw/20260927T081503Z-thuan-mac-1/reference/coffee coldbrew_4daf9729-9636-5534-8214-749f5664cd5b.svg'
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
        poly(self,'glass',(4,16),(28,16),(44,16),(44,38),(40,40),(8,40),(4,38),(4,16))
        poly(self,'straw',(28,16),(32,8),(44,8))
        for i,x in enumerate((12,28)):
         poly(self,f'ice-{i}',(x,24),(x+8,24),(x+8,32),(x,32),(x,24))
        contacts(self)
