"""A raised hand points its index finger upward while the remaining fingers curl beside it. A diagonal band crosses the extended fingertip, and a rectangular cuff finishes the wrist.
Lucide pointer and hand construction inform the rounded fingertip, curled knuckle group and palm. Diagonal bandage seam and rectangular cuff retain identity. Individual curled-finger creases omitted; intentional thumb-side asymmetry.
VRECT_L: centerline extremes (8,6)-(40,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '806acf8e-3fa3-5523-a16c-605e6d202d8b'
SOURCE_PATH = 'pictographic-primitives/work/task finger bandage_806acf8e-3fa3-5523-a16c-605e6d202d8b.svg'
AUTHOR = 'gpt-6'

class BandagedIndexFingerVariant2(Solo48):
    icon_id = 'bandaged-index-finger-v2'
    variant_of = 'bandaged-index-finger'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('hand', 'finger', 'bandage', 'injury', 'pointing', 'care')

    def build(self) -> None:
        self.add_arc('fingertip', (22, 9), (32, 9), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('index-upper', (32, 9), (32, 12))
        self.add_line('index-lower', (32, 12), (32, 20))
        self.add_line('knuckles', (32, 20), (34, 20))
        self.add_arc('knuckle-round', (34, 20), (40, 26), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('palm-side', (40, 26), (40, 30))
        self.add_arc('palm-round', (40, 30), (34, 36), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('wrist-top', (34, 36), (18, 36))
        self.add_line('thumb-heel', (18, 36), (12, 36))
        self.add_line('thumb-outer', (12, 36), (8, 30))
        self.add_line('thumb-wall', (8, 30), (8, 25))
        self.add_arc('thumb-tip', (8, 25), (14, 25), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('thumb-inner', (14, 25), (22, 30))
        self.add_line('index-left-lower', (22, 30), (22, 18))
        self.add_line('index-left-upper', (22, 18), (22, 9))
        self.add_contour('hand', 'fingertip', 'index-upper', 'index-lower', 'knuckles', 'knuckle-round', 'palm-side', 'palm-round', 'wrist-top', 'thumb-heel', 'thumb-outer', 'thumb-wall', 'thumb-tip', 'thumb-inner', 'index-left-lower', 'index-left-upper', closed=True)
        self.add_line('bandage-seam', (22, 18), (32, 12))
        self.relate('connect', 'bandage-seam', 'hand')
        self.add_polyline('cuff', (18, 36), (18, 44), (34, 44), (34, 36), closed=False)
        self.relate('connect', 'cuff', 'hand')
