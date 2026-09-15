# Review candidate; original preserved.
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
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('bird', 'singing', 'beak', 'open', 'song', 'chirp', 'head', 'wildlife')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('head-top',(8, 27),*(((8, 20.19335832), (11.91012058, 14.52356025), (18, 14)),))
        self.add_arc('forehead',(18, 14),(30, 22),radius_x=12,radius_y=8,large_arc=False,sweep=True)
        self.add_line('upper-beak',(30, 22),(40, 15))
        self.add_line('mouth-top',(40, 15),(31, 30))
        self.add_line('mouth-bottom',(31, 30),(40, 33))
        self.add_line('lower-beak',(40, 33),(29, 40))
        self.add_line('breast',(29, 40),(30, 44))
        self.add_bezier('nape',(8, 27),*(((8, 31.10187803), (8.29530241, 35.5180598), (10, 40)),))
        self.add_line('neck-back',(10, 40),(8, 44))
        self.add_line('beak-crown',(18, 14),(25, 4))
        self.add_line('beak-rise',(25, 4),(30, 22))
        self.add_line('eye',(17, 26),(17, 26))
        self.add_contour('front',*('head-top', 'forehead', 'upper-beak', 'mouth-top', 'mouth-bottom', 'lower-beak', 'breast'),closed=False)
        self.add_contour('back',*('nape', 'neck-back'),closed=False)
        self.add_contour('crown',*('beak-crown', 'beak-rise'),closed=False)
        self.relate('connect',*('front', 'back'))
        self.relate('connect',*('front', 'crown'))
