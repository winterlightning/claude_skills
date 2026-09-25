"""Broad molar with two rounded roots. VRECT_L (8,4)-(40,44).
One closed contour owns crown, sides and root opening; mirrored about x=24.
Source supplies shallow crown dip and two long roots. No useful Lucide tooth
match exists. No identity-carrying detail is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bd3ed1c5-f392-45bf-ac8f-4f6eb786cbd1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/molar_bd3ed1c5-f392-45bf-ac8f-4f6eb786cbd1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'broad-molar-with-two-rounded-roots'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Dental Molar Tooth Symbol',)
    keywords = ('molar','tooth','dental','roots','crown','teeth','anatomy')
    def build(self):
        axis=24
        left=[((24,7),(21,7),(18,4),(15,4)),
              ((15,4),(10,4),(8,8),(8,14)),
              ((8,14),(8,24),(10,44),(16,44)),
              ((16,44),(21,44),(18,28),(24,28))]
        curves=left+[tuple((2*axis-x,y) for x,y in reversed(c)) for c in reversed(left)]
        for j,(a,c1,c2,z) in enumerate(curves):self.add_bezier(f'outline-{j}',a,(c1,c2,z))
        self.add_contour('tooth',*[f'outline-{j}' for j in range(len(curves))],closed=True)
