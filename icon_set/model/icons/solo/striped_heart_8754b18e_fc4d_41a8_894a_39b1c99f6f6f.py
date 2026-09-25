"""A broad heart with three horizontal stripes; paired radius-9 lobes mirror across x=24.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8754b18e-fc4d-41a8-894a-39b1c99f6f6f'
SOURCE_PATH = 'pictographic-primitives/romance/lesbian lgbt heart_8754b18e-fc4d-41a8-894a-39b1c99f6f6f.svg'
AUTHOR = 'gpt-6'


class StripedHeart(Solo48):
    icon_id = 'striped-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    aliases = ()
    keywords = ('heart', 'stripe', 'lgbt', 'pride', 'love', 'romance')

    def build(self) -> None:
        self.add_arc('lobe-l',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_arc('shoulder-l',(6,15),(10,23),radius_x=10,sweep=False)
        for i,(a,b) in enumerate(zip([(10,23),(16,31),(24,42),(32,31)],[(16,31),(24,42),(32,31),(38,23)]),1):
            self.add_line(f'point-{i}',a,b)
        self.add_arc('shoulder-r',(38,23),(42,15),radius_x=10,sweep=False)
        self.add_arc('lobe-r',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','lobe-l','shoulder-l','point-1','point-2','point-3','point-4','shoulder-r','lobe-r',closed=True)
        for n,y,left,right in [('top',15,6,42),('middle',23,10,38),('bottom',31,16,32)]:
            self.add_line(n,(left,y),(right,y))
            self.relate('connect','heart',n)
