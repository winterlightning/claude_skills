"""Protective Safety Work Glove.
Plan: Four rounded fingertips and a left spread thumb above a broad cuff. Extrema (4,8)-(44,40).
Reference: Lucide hand: rounded fingers with shared interior separations and broad palm; human reference governs minimal anatomy.
Reduction: Diagonal orientation made upright to keep four rounded fingers readable; cuff edge retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e60f0c02-0f0a-45cd-afaa-1f3a71bcc802'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__work-glove-spread-thumb/20260927T082307Z-thuan-mac-1/reference/glove_e60f0c02-0f0a-45cd-afaa-1f3a71bcc802.svg'
AUTHOR = "gpt-6"

class Batch29Icon(Solo48):
    icon_id = 'work-glove-spread-thumb'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('protective', 'safety', 'work', 'glove')

    def build(self):
        # Diagonal spread-thumb glove: a single continuous palm and two raised tips.
        self.add_line('cuff-left',(22,42),(6,32))
        self.add_line('thumb-base',(6,32),(12,26))
        self.add_line('thumb-outer',(12,26),(16,10))
        self.add_bezier('thumb-tip',(16,10),((17,7),(20,7),(21,10)))
        self.add_line('thumb-inner',(21,10),(20,19))
        self.add_line('finger-left',(20,19),(34,6))
        self.add_bezier('finger-tip',(34,6),((37,6),(40,7),(40,10)))
        self.add_line('finger-side',(40,10),(42,18))
        self.add_line('palm-side',(42,18),(32,32))
        self.add_line('cuff-right',(32,32),(22,42))
        self.add_contour('glove','cuff-left','thumb-base','thumb-outer','thumb-tip','thumb-inner','finger-left','finger-tip','finger-side','palm-side','cuff-right',closed=True)
