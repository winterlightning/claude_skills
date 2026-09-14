# Variant of cowboy-hat-with-band; parent file remains unchanged.
"""A cowboy hat with a dipped crown and upturned brim. HRECT_L extremes (2,8)-(46,40). Lucide hat-glasses informs the tapered crown; the supplied western brim is preserved. Symmetric construction with deliberate crown corners."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '40c003ad-799f-5db4-a0f5-1e7b1ad0ad75'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/hat cowboy_40c003ad-799f-5db4-a0f5-1e7b1ad0ad75.svg'
AUTHOR = 'gpt-6'

class CowboyHatWithBandVariant2(Solo48):
    icon_id = 'cowboy-hat-with-band-v2'
    variant_of = 'cowboy-hat-with-band'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('hat', 'cowboy hat', 'western', 'stetson', 'hatband', 'brim', 'ranch', 'headwear')

    def build(self) -> None:
        self.add_line('crown-left', (11, 28), (15, 12))
        self.add_arc('shoulder-left', (15, 12), (19, 8), radius_x=4)
        self.add_line('dip-left', (19, 8), (24, 11))
        self.add_line('dip-right', (24, 11), (29, 8))
        self.add_arc('shoulder-right', (29, 8), (33, 12), radius_x=4)
        self.add_line('crown-right', (33, 12), (37, 28))
        self.add_contour('crown', 'crown-left', 'shoulder-left', 'dip-left', 'dip-right', 'shoulder-right', 'crown-right')
        self.add_polyline('brim-top', (4, 24), (11, 28), (37, 28), (44, 24))
        self.add_arc('brim-base', (44, 24), (4, 24), radius_x=20, radius_y=16)
        self.relate('connect', 'brim-top', 'brim-base')
        self.relate('connect', 'crown', 'brim-top')
