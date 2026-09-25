"""A pillar candle with a heart flame sits in a rounded holder; one broad wax drip remains.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38fd3f15-701d-4404-8da0-af7c79ef4dd2'
SOURCE_PATH = 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg'
AUTHOR = 'gpt-6'


class CandleWithHeartFlame(Solo48):
    icon_id = 'candle-with-heart-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    aliases = ()
    keywords = ('candle', 'heart', 'flame', 'wax', 'holder', 'romance')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        heart('flame',24,8,4,18)
        self.add_line('wick',(24,18),(24,20))
        self.relate('connect','flame','wick')
        self.add_polyline('candle',(14,36),(14,28),(14,20),(24,20),(34,20),(34,28),(34,36))
        self.relate('connect','wick','candle')
        self.add_line('wax-l',(14,28),(18,28))
        self.add_arc('wax-drip',(18,28),(26,28),radius_x=4,sweep=False)
        self.add_line('wax-r',(26,28),(34,28))
        self.add_contour('wax','wax-l','wax-drip','wax-r')
        self.relate('connect','wax','candle')
        self.add_line('holder-top',(8,36),(40,36))
        self.add_arc('holder-r',(40,36),(32,44),radius_x=8)
        self.add_line('holder-base',(32,44),(16,44))
        self.add_arc('holder-l',(16,44),(8,36),radius_x=8)
        self.add_contour('holder','holder-top','holder-r','holder-base','holder-l',closed=True)
        self.relate('connect','candle','holder')
