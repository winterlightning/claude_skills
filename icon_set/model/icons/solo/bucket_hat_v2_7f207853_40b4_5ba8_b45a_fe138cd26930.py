# Variant of bucket-hat; parent file remains unchanged.
'bucket-hat: Repositioned the outer contours to the exact keyshape width while retaining the defining details. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f207853-40b4-5ba8-b45a-fe138cd26930'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/hat retro_7f207853-40b4-5ba8-b45a-fe138cd26930.svg'
AUTHOR = 'gpt-6'

class BucketHatVariant2(Solo48):
    icon_id = 'bucket-hat-v2'
    variant_of = 'bucket-hat'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('hat', 'bucket hat', 'cloche', 'sun hat', 'retro', 'brim', 'headwear', 'fashion')

    def build(self) -> None:
        self.add_arc('dome', (10, 24), (38, 24), radius_x=14, radius_y=16, sweep=True)
        self.add_line('crown-r', (38, 24), (38, 27))
        self.add_arc('crown-base', (38, 27), (10, 27), radius_x=14, radius_y=3, sweep=True)
        self.add_line('crown-l', (10, 27), (10, 24))
        self.add_contour('crown', 'dome', 'crown-r', 'crown-base', 'crown-l', closed=True)
        self.add_line('flare-r', (38, 27), (44, 36))
        self.add_arc('hem', (44, 36), (4, 36), radius_x=20, radius_y=4, sweep=True)
        self.add_line('flare-l', (4, 36), (10, 27))
        self.add_contour('brim', 'flare-r', 'hem', 'flare-l', closed=False)
        self.relate('connect', 'brim', 'crown')
