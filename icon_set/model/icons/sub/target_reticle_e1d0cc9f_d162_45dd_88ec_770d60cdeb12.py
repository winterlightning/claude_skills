"""Target Reticle: A circular outline has short crosshair ticks at its top, bottom, left, and right. A tiny central dot sits between the four inward-facing tick ends.

Construction: Circular reticle with four cardinal ticks crossing its edge and a centred dot.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e1d0cc9f-d162-45dd-88ec-770d60cdeb12'
SOURCE_PATH = 'pictographic-primitives/state/target dot_e1d0cc9f-d162-45dd-88ec-770d60cdeb12.svg'
AUTHOR = 'gpt-6'


class TargetReticle(Sub32):
    icon_id = 'target-reticle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('target', 'reticle', 'circular', 'outline', 'short', 'crosshair', 'ticks', 'top')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle("ring",16,16,11)
        for name,a,b in (("top",(16,2),(16,8)),("bottom",(16,24),(16,30)),("left",(2,16),(8,16)),("right",(24,16),(30,16))):
            self.add_line(name,a,b)
            self.relate("connect","ring",name)
        self.add_dot("centre",(16,16))
