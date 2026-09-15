"""Therapist bust in crossover robe. Square extremes 6,6–42,42. Shared circular head and mirrored shoulder radii from Lucide user-round; directional wrap; omit sleeve seams."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa9fac7c-8bae-51fb-a78a-596a33f60631'
SOURCE_PATH = 'pictographic-primitives/spas/spa therapist robe_aa9fac7c-8bae-51fb-a78a-596a33f60631.svg'
AUTHOR = 'gpt-6'

class SpaTherapistInWrapRobe(Solo48):
    icon_id = 'spa-therapist-in-wrap-robe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/wellness"
    aliases = ()
    keywords = ('spa', 'wellness', 'spa-therapist-in-wrap-robe')

    def build(self):
        self.add_arc('head-top', (18,12), (30,12), radius_x=6, radius_y=6)
        self.add_arc('head-bottom', (30,12), (18,12), radius_x=6, radius_y=6)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('left-side', (6,42), (6,36))
        self.add_arc('left-shoulder', (6,36), (16,26), radius_x=10)
        self.add_contour('left', 'left-side', 'left-shoulder')
        self.add_arc('right-shoulder', (32,26), (42,36), radius_x=10)
        self.add_line('right-side', (42,36), (42,42))
        self.add_contour('right', 'right-shoulder', 'right-side')
        self.add_polyline('wrap', (32,26), (16,42), (33,42))
        self.add_line('lapel', (16,26), (24,34))
        self.relate('connect', 'left', 'lapel')
        self.relate('connect', 'right', 'wrap')
        self.relate('connect', 'lapel', 'wrap')
