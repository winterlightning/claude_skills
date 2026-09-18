# Variant of dna-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of dna.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b4ea616c-9fe4-40b2-ab7c-11c82b439358'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4ea616c-9fe4-40b2-ab7c-11c82b439358', 'pictographic-primitives/artificial-intelligence/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dna',)
SOLO_SOURCE_ICON_IDS = ('dna',)
REFERENCE_EXPORT_SHA256 = '7db5f99141f12a42d646294f38bdb1222ec98b9dbe2e6ab804818860f265ef57'

class DrawingVariant3(Sub32):
    icon_id = 'dna-sub32-v3'
    variant_of = 'dna-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Two reflected strands share exact rung attachments and a central crossing.
        for tag,sign in [('a',1),('b',-1)]:
         def p(x,y):return (16+sign*(x-16),y)
         self.add_bezier(tag+'top',p(6,2),(p(6,4),p(6,5),p(7,7)))
         self.add_bezier(tag+'middle',p(7,7),(p(11,15),p(21,17),p(25,25)))
         self.add_bezier(tag+'bottom',p(25,25),(p(26,27),p(26,28),p(26,30)))
         self.add_contour(tag,tag+'top',tag+'middle',tag+'bottom')
        self.relate('connect','a','b')
        for y in [7,25]:
         uid='rung-'+str(y);self.add_line(uid,(7,y),(25,y))
         self.relate('connect',uid,'a');self.relate('connect',uid,'b')
