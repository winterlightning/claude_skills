"""Three cake tiers with rounded upper corners step outward; one scalloped icing band replaces fine bands.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e53fed3c-e8be-5f6e-be19-653459eccf74'
SOURCE_PATH = 'pictographic-primitives/romance/wedding cake_e53fed3c-e8be-5f6e-be19-653459eccf74.svg'
AUTHOR = 'gpt-6'


class ThreeTierWeddingCake(Solo48):
    icon_id = 'three-tier-wedding-cake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('cake', 'wedding', 'tier', 'icing', 'dessert', 'celebration')

    def build(self) -> None:
        def tier(n,left,right,top,bottom):
            r=2
            self.add_line(n+'-l',(left,bottom),(left,top+r))
            self.add_arc(n+'-tl',(left,top+r),(left+r,top),radius_x=r)
            self.add_line(n+'-t',(left+r,top),(right-r,top))
            self.add_arc(n+'-tr',(right-r,top),(right,top+r),radius_x=r)
            self.add_line(n+'-r',(right,top+r),(right,bottom))
            self.add_line(n+'-b',(right,bottom),(left,bottom))
            self.add_contour(n,n+'-l',n+'-tl',n+'-t',n+'-tr',n+'-r',n+'-b',closed=True)
        tier('top-tier',16,32,6,16)
        tier('middle-tier',10,38,16,28)
        tier('bottom-tier',6,42,28,42)
        self.relate('connect','top-tier','middle-tier')
        self.relate('connect','middle-tier','bottom-tier')
        for i,x in enumerate((6,18,30)):
            self.add_arc(f'icing-{i}',(x,34),(x+12,34),radius_x=6,radius_y=3,sweep=False)
        self.add_contour('icing',*(f'icing-{i}' for i in range(3)))
        self.relate('connect','icing','bottom-tier')
