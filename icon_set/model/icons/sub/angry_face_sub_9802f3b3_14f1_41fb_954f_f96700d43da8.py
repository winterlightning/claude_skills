"""Angry Face: A circular face has sharply inward-slanting eyebrows above tiny eyes and a small downturned mouth. The brows form the strongest interior marks, giving the balanced face a stern expression.

Construction: Circular expression with inward angled eye strokes and an arched frown; paired features mirror.
Keyshape: CIRCLE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9802f3b3-14f1-41fb-954f-f96700d43da8'
SOURCE_PATH = 'pictographic-primitives/state/face angry_9802f3b3-14f1-41fb-954f-f96700d43da8.svg'
AUTHOR = 'gpt-6'


class AngryFaceSub(Sub32):
    icon_id = 'angry-face-sub'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('angry', 'face', 'circular', 'sharply', 'inward', 'slanting', 'eyebrows', 'tiny')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle("face",16,16,14)
        self.add_line("eye-left",(10,11),(12,13))
        self.add_line("eye-right",(20,13),(22,11))
        self.add_arc("frown",(11,21),(21,21),radius_x=5,radius_y=2)
