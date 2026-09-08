"""A domed bucket hat with a flared brim; underside ellipse omitted for clear spacing."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f207853-40b4-5ba8-b45a-fe138cd26930'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/hat retro_7f207853-40b4-5ba8-b45a-fe138cd26930.svg'
AUTHOR = 'astra-chatgpt'


class BucketHat(Solo48):
    icon_id = 'bucket-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('hat', 'bucket hat', 'cloche', 'sun hat', 'retro', 'brim', 'headwear', 'fashion')

    def build(self) -> None:
        # HRECT_L: authored directly to its SOLO48 centerline extremes.
        self.add_arc('dome', (10, 24), (38, 24), radius_x=14, radius_y=16, sweep=True)
        self.add_line('crown-r', (38, 24), (38, 27))
        self.add_arc('crown-base', (38, 27), (10, 27), radius_x=14, radius_y=3, sweep=True)
        self.add_line('crown-l', (10, 27), (10, 24))
        self.add_contour('crown', 'dome', 'crown-r', 'crown-base', 'crown-l', closed=True)
        self.add_line('flare-r', (38, 27), (46, 36))
        self.add_arc('hem', (46, 36), (2, 36), radius_x=22, radius_y=4, sweep=True)
        self.add_line('flare-l', (2, 36), (10, 27))
        self.add_contour('brim', 'flare-r', 'hem', 'flare-l', closed=False)
        self.relate("connect", 'brim', 'crown')
