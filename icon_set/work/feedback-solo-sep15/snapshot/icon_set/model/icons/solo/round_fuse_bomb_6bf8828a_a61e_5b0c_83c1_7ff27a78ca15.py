"""Round Fuse Bomb. Lucide bomb informed circular body; curved fuse replaces small neck collar.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6bf8828a-a61e-5b0c-83c1-7ff27a78ca15'
SOURCE_PATH = 'pictographic-primitives/war/bomb_6bf8828a-a61e-5b0c-83c1-7ff27a78ca15.svg'
AUTHOR = 'gpt-6'

class RoundFuseBomb(Solo48):
    icon_id = 'round-fuse-bomb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('bomb', 'fuse', 'round', 'explosive', 'weapon', 'sphere')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('bodya',(8, 28),*(((8, 19.163444), (15.163444, 11.5), (24.0, 11.5)), ((32.836556, 11.5), (40, 19.163444), (40, 28))))
        self.add_arc('bodyb',(40, 28),(8, 28),radius_x=16,radius_y=16,large_arc=False,sweep=True)
        self.add_line('neck',(24, 12),(24, 9))
        self.add_bezier('fuse-rise',(24, 9),*(((24.88631641, 5.84935233), (27.33247694, 4), (30, 4)),))
        self.add_bezier('fuse-fall',(30, 4),*(((32.66752306, 4), (35.11368359, 5.84935233), (36, 9)),))
        self.add_contour('body',*('bodya', 'bodyb'),closed=True)
        self.add_contour('fuse',*('fuse-rise', 'fuse-fall'),closed=False)
        self.relate('connect',*('neck', 'body'))
        self.relate('connect',*('fuse', 'neck'))
