"""Frontal squid with a pointed mantle, paired fins and four curling arms. Bounds (2,2)-(46,46). Mirror construction about x=24; omit collar band and two crowded arms. No useful local squid match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b1b950d-cc96-5942-b04e-c7eb45776f56'
SOURCE_PATH = 'pictographic-primitives/animals/squid_6b1b950d-cc96-5942-b04e-c7eb45776f56.svg'
AUTHOR = 'gpt-6'


class Squid(Solo48):
    icon_id = 'squid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('squid', 'tentacles', 'sea', 'ocean', 'marine', 'cephalopod', 'fins', 'calamari')

    def build(self) -> None:
        self.add_line('mantle-left',(14,28),(14,20))
        self.add_arc('fin-left',(14,20),(8,16),radius_x=6,sweep=True)
        self.add_arc('point-left',(8,16),(24,2),radius_x=32,sweep=True)
        self.add_arc('point-right',(24,2),(40,16),radius_x=32,sweep=True)
        self.add_arc('fin-right',(40,16),(34,20),radius_x=6,sweep=True)
        self.add_line('mantle-right',(34,20),(34,28))
        self.add_contour('mantle','mantle-left','fin-left','point-left','point-right','fin-right','mantle-right')
        self.add_line('collar',(14,28),(34,28))
        self.relate('connect','mantle','collar')
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            tag='left' if side<0 else 'right'
            self.add_arc(tag+'-outer-arm',p(10,28),p(22,38),radius_x=12,radius_y=10,sweep=(side<0))
            self.relate('connect',tag+'-outer-arm','mantle')
            self.relate('connect',tag+'-outer-arm','collar')
            self.add_line(tag+'-inner-root',p(4,28),p(4,38))
            self.add_arc(tag+'-inner-curl',p(4,38),p(12,46),radius_x=8,sweep=(side<0))
            self.add_contour(tag+'-inner-arm',tag+'-inner-root',tag+'-inner-curl')
            self.relate('connect',tag+'-inner-arm','collar')
