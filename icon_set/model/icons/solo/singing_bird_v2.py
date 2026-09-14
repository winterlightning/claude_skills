# Variant of singing-bird; parent file remains unchanged.
'A singing bird with its triangular crest removed. HRECT_XL extremes (6,6)-(42,42) fit the remaining head and open bill without the crest. Lucide bird informs a smooth domed head and sparse dot eye. The open-beak side profile is intentionally asymmetric.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '100799e2-7de7-58f9-a91a-cf91475c62fe'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird sing_100799e2-7de7-58f9-a91a-cf91475c62fe.svg'
AUTHOR = 'gpt-6'

class SingingBirdVariant2(Solo48):
    icon_id = 'singing-bird-v2'
    variant_of = 'singing-bird'
    variant_label = 'Remove triangular crest'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('bird', 'singing', 'beak', 'open', 'song', 'chirp', 'head', 'wildlife')

    def build(self) -> None:
        self.add_arc('head-top', (6, 27), (18, 6), radius_x=16, radius_y=22, sweep=True)
        self.add_arc('forehead', (18, 6), (30, 22), radius_x=12, radius_y=17, sweep=True)
        self.add_line('upper-beak', (30, 22), (42, 15))
        self.add_line('mouth-top', (42, 15), (31, 30))
        self.add_line('mouth-bottom', (31, 30), (42, 33))
        self.add_line('lower-beak', (42, 33), (29, 39))
        self.add_line('breast', (29, 39), (30, 42))
        self.add_contour('front', 'head-top', 'forehead', 'upper-beak', 'mouth-top', 'mouth-bottom', 'lower-beak', 'breast', closed=False)
        self.add_arc('nape', (6, 27), (8, 39), radius_x=26, radius_y=26, sweep=False)
        self.add_line('neck-back', (8, 39), (6, 42))
        self.add_contour('back', 'nape', 'neck-back', closed=False)
        self.relate('connect', 'front', 'back')
        self.add_dot('eye', (17, 26))
