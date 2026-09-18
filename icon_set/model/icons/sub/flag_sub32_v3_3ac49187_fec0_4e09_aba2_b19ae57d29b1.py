# Variant of flag-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of flag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3ac49187-fec0-4e09-aba2-b19ae57d29b1'
SOURCE_PATH = 'pictographic-primitives/social/flag_3ac49187-fec0-4e09-aba2-b19ae57d29b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ac49187-fec0-4e09-aba2-b19ae57d29b1', 'pictographic-primitives/social/flag_3ac49187-fec0-4e09-aba2-b19ae57d29b1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flag',)
SOLO_SOURCE_ICON_IDS = ('flag',)
REFERENCE_EXPORT_SHA256 = 'da12d6216d72f07d2d547a551af2902c8d08e57dd8be3314ac2c129b92bfbd0d'

class DrawingVariant3(Sub32):
    icon_id = 'flag-sub32-v3'
    variant_of = 'flag-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'social'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Flag cloth with an intentional visible wave, coherent top and bottom curves, and a straight pole.
        self.add_line('pole',(6,2),(6,30));self.add_line('foot',(4,30),(10,30));self.relate('connect','pole','foot')
        self.add_bezier('wave-top',(6,7),((14,2),(20,12),(28,7)))
        self.add_line('fly',(28,7),(28,19))
        self.add_bezier('wave-bottom',(28,19),((20,24),(14,14),(6,19)))
        self.add_contour('cloth','wave-top','fly','wave-bottom')
        self.relate('connect','pole','cloth')
