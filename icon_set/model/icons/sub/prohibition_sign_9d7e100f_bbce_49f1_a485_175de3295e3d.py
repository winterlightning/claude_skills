"""Prohibition Sign: A circular outline contains a straight diagonal slash running from lower left to upper right. The slash joins the outer ring at both ends and divides its empty interior.

Construction: Circle and rising slash intentionally cross; slash extends slightly outside ring.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9d7e100f-bbce-49f1-a485-175de3295e3d'
SOURCE_PATH = 'pictographic-primitives/state/cancel_9d7e100f-bbce-49f1-a485-175de3295e3d.svg'
AUTHOR = 'gpt-6'


class ProhibitionSign(Sub32):
    icon_id = 'prohibition-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('prohibition', 'sign', 'circular', 'outline', 'contains', 'straight', 'diagonal', 'slash')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle("ring",16,16,12)
        self.add_line("slash",(2,30),(30,2))
        self.relate("connect","ring","slash")
