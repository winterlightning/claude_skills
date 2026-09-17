"""Crosshair: A circle is crossed centrally by long horizontal and vertical lines. Both lines extend beyond the circumference on opposite sides, creating four evenly spaced outward arms.

Construction: Circular target with two true crossing diameter strokes extending beyond the circle.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '59c73500-c4b0-4115-a297-9f035d6469b6'
SOURCE_PATH = 'pictographic-primitives/state/target 5_59c73500-c4b0-4115-a297-9f035d6469b6.svg'
AUTHOR = 'gpt-6'


class CrosshairSub(Sub32):
    icon_id = 'crosshair-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('crosshair', 'circle', 'crossed', 'centrally', 'long', 'horizontal', 'vertical', 'lines')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle("ring",16,16,10)
        self.add_line("horizontal",(2,16),(30,16))
        self.add_line("vertical",(16,2),(16,30))
        self.relate("connect","ring","horizontal")
        self.relate("connect","ring","vertical")
        self.relate("connect","horizontal","vertical")
