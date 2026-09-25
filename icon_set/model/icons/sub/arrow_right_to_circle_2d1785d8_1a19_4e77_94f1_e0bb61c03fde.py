"""Arrow Right to Circle: A horizontal arrow points right toward a separate small circular outline. The circle sits directly ahead of the open arrowhead, with a visible gap between them.

Construction: A horizontal arrow ends before a separate outlined circular target.
Keyshape: HRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2d1785d8-1a19-4e77-94f1-e0bb61c03fde'
SOURCE_PATH = 'pictographic-primitives/state/arrow right with circle_2d1785d8-1a19-4e77-94f1-e0bb61c03fde.svg'
AUTHOR = 'gpt-6'


class ArrowRightToCircle(Sub32):
    icon_id = 'arrow-right-to-circle'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('arrow', 'right', 'circle', 'horizontal', 'points', 'toward', 'separate', 'small')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        self.add_line('shaft',(2,16),(16,16))
        self.add_polyline('head',(10,10),(16,16),(10,22))
        self.relate('connect','shaft','head')
        circle('target',26,16,4)
