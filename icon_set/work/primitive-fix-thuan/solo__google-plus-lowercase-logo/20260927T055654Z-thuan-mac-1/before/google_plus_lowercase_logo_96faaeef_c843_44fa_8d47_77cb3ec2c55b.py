"""A lowercase double-storey g with a tall round upper bowl, an ear stroke at the top right and a large oval lower loop, followed by a plus sign at mid height.

Plan: Double-storey g with a wider upper bowl, flat ear, curved neck and lower oval; plus at mid-height.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; shared ellipse and letter attachment geometry.
Simplification: Colour omitted; wider bowl and lower plus distinguish this supplied variant.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96faaeef-c843-44fa-8d47-77cb3ec2c55b'
SOURCE_PATH = 'pictographic-primitives/logos/google plus logo 2_96faaeef-c843-44fa-8d47-77cb3ec2c55b.svg'
AUTHOR = 'gpt-6'


class GooglePlusLowercaseLogo(Solo48):
    icon_id = 'google-plus-lowercase-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-plus', 'google', 'social', 'letter-g', 'plus', 'logo', 'brand')

    def build(self):
        # Flat ear joins a straight shoulder, avoiding a pinched tangent overlap.
        cx, rx = 14, 8
        self.add_line('bowl-top',(10,8),(cx+rx,8))
        self.add_line('bowl-right',(cx+rx,8),(cx+rx,15))
        self.add_arc('bowl-bottom-right',(cx+rx,15),(cx,22),radius_x=rx,radius_y=7)
        self.add_arc('bowl-bottom-left',(cx,22),(cx-rx,15),radius_x=rx,radius_y=7)
        self.add_line('bowl-left',(6,15),(6,12))
        self.add_arc('bowl-corner',(6,12),(10,8),radius_x=4)
        self.add_contour('bowl','bowl-top','bowl-right','bowl-bottom-right','bowl-bottom-left','bowl-left','bowl-corner',closed=True)
        self.add_line('ear',(cx+rx,8),(25,8))
        self.relate('connect','bowl','ear')
        self.add_arc('loop-a',(14,30),(24,35),radius_x=10,radius_y=5)
        self.add_arc('loop-b',(24,35),(4,35),radius_x=10,radius_y=5)
        self.add_arc('loop-c',(4,35),(14,30),radius_x=10,radius_y=5)
        self.add_contour('loop','loop-a','loop-b','loop-c',closed=True)
        self.add_bezier('link',(cx,22),((cx-5,25),(cx-5,28),(14,30)))
        self.relate('connect','bowl','link')
        self.relate('connect','loop','link')
        self.add_polyline('plus-h',(34,24),(39,24),(44,24))
        self.add_polyline('plus-v',(39,24-5),(39,24),(39,24+5))
        self.relate('connect','plus-h','plus-v')
