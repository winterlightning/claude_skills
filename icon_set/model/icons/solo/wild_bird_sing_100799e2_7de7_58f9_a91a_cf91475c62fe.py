"""singing-bird: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape VRECT_XL; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '100799e2-7de7-58f9-a91a-cf91475c62fe'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird sing_100799e2-7de7-58f9-a91a-cf91475c62fe.svg'
AUTHOR = 'gpt-6'


class SingingBird(Solo48):
    icon_id = 'singing-bird'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('bird', 'singing', 'beak', 'open', 'song', 'chirp', 'head', 'wildlife')

    def build(self) -> None:
        self.add_arc('head-top', (5, 27), (18, 14), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('forehead', (18, 14), (30, 22), radius_x=12, radius_y=8, sweep=True)
        self.add_line('upper-beak', (30, 22), (43, 15))
        self.add_line('mouth-top', (43, 15), (31, 30))
        self.add_line('mouth-bottom', (31, 30), (43, 33))
        self.add_line('lower-beak', (43, 33), (29, 39))
        self.add_line('breast', (29, 39), (30, 46))
        self.add_contour('front', 'head-top', 'forehead', 'upper-beak', 'mouth-top', 'mouth-bottom', 'lower-beak', 'breast', closed=False)
        self.add_arc('nape', (5, 27), (8, 39), radius_x=26, radius_y=26, sweep=False)
        self.add_line('neck-back', (8, 39), (5, 46))
        self.add_contour('back', 'nape', 'neck-back', closed=False)
        self.relate("connect", 'front', 'back')
        self.add_line('beak-crown', (18, 14), (23, 2))
        self.add_line('beak-rise', (23, 2), (30, 22))
        self.add_contour('crown', 'beak-crown', 'beak-rise', closed=False)
        self.relate("connect", 'front', 'crown')
        self.add_dot('eye', (17, 26))
