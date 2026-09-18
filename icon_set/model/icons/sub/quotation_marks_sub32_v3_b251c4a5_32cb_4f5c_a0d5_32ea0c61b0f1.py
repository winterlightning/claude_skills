# Variant of quotation-marks-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of quotation-marks.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1'
SOURCE_PATH = 'pictographic-primitives/symbol/quotation_b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1', 'pictographic-primitives/symbol/quotation_b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/quotation-marks',)
SOLO_SOURCE_ICON_IDS = ('quotation-marks',)
REFERENCE_EXPORT_SHA256 = 'adaa7483df1701cdba3333d8a8a988feabc06489831545d5495d5d881015379a'

class DrawingVariant3(Sub32):
    icon_id = 'quotation-marks-sub32-v3'
    variant_of = 'quotation-marks-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Opening quotation marks with compact bowls and smooth tails; avoid oversized circular sixes.
        for i,x in enumerate([2,20]):
         p=f'q{i}-'
         self.add_bezier(p+'tail',(x+10,4),((x+3,7),(x,13),(x,20)))
         self.add_line(p+'top',(x,20),(x+6,20))
         self.add_arc(p+'right',(x+6,20),(x+6,28),radius_x=4,radius_y=4,sweep=True)
         self.add_line(p+'base',(x+6,28),(x+4,28))
         self.add_arc(p+'left',(x+4,28),(x,24),radius_x=4,radius_y=4,sweep=True)
         self.add_line(p+'stem',(x,24),(x,20))
         self.add_contour(p+'bowl',p+'top',p+'right',p+'base',p+'left',p+'stem',closed=True)
         self.relate('connect',p+'tail',p+'bowl')
