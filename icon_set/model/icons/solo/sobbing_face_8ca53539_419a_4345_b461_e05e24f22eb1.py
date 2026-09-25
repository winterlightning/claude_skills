"""Sobbing Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ca53539-419a-4345-b461-e05e24f22eb1'
SOURCE_PATH = 'pictographic-primitives/smileys/crying rainbow_8ca53539-419a-4345-b461-e05e24f22eb1.svg'
AUTHOR = 'gpt-6'


class SobbingFace(Solo48):
    icon_id = 'sobbing-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('sobbing', 'crying', 'tears', 'wailing', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE ink (4,4)-(44,44); tear streams interrupt the cheek outline.
        self.add_arc("head-top",(6,24),(42,24),radius_x=18)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y): return (24+sign*(x-24),y)
            self.add_arc(f"eye-{side}",p(16,19),p(19,19),radius_x=4,sweep=sign>0)
            self.add_line(f"tear-{side}",p(12,30),p(12,38))
            self.add_arc(f"pool-{side}",p(12,38),p(8,42),radius_x=4,sweep=sign>0)
            self.add_line(f"pool-end-{side}",p(8,42),p(6,42))
            self.add_contour(f"stream-{side}",f"tear-{side}",f"pool-{side}",f"pool-end-{side}")
        self.add_arc("mouth-top",(21,30),(27,30),radius_x=3)
        self.add_arc("mouth-bottom",(27,30),(21,30),radius_x=3)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
