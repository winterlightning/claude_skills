# Variant of flame-59aa3cfd-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of flame-59aa3cfd.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1'
SOURCE_PATH = 'pictographic-primitives/products/flame_59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1', 'pictographic-primitives/products/flame_59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame-59aa3cfd',)
SOLO_SOURCE_ICON_IDS = ('flame-59aa3cfd',)
REFERENCE_EXPORT_SHA256 = '3218057023c3d16ce533700b62b7417f15ec19faf503dfe7dca76fa4623d8b28'

class DrawingVariant3(Sub32):
    icon_id = 'flame-59aa3cfd-sub32-v3'
    variant_of = 'flame-59aa3cfd-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'products'
    categories = ('primitives', 'products')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Restore the flame’s leaning tip and asymmetric growth; avoid a symmetric onion shape.
        self.add_bezier('right-upper',(13,2),((16,8),(26,13),(26,20)))
        self.add_bezier('right-base',(26,20),((26,26),(22,30),(16,30)))
        self.add_bezier('left-base',(16,30),((10,30),(6,26),(6,20)))
        self.add_bezier('left-upper',(6,20),((6,13),(15,10),(13,2)))
        self.add_contour('flame','right-upper','right-base','left-base','left-upper',closed=True)
