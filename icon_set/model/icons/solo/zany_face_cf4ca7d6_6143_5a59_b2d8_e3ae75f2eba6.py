"""Zany Face. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf4ca7d6-6143-5a59-b2d8-e3ae75f2eba6'
SOURCE_PATH = 'pictographic-primitives/smileys/crazy_cf4ca7d6-6143-5a59-b2d8-e3ae75f2eba6.svg'
AUTHOR = 'gpt-6'


class ZanyFace(Solo48):
    icon_id = 'zany-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('zany', 'crazy', 'tongue', 'grin', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        self.add_polyline("eye-left-down",(15,17),(17,19),(19,21))
        self.add_polyline("eye-left-up",(15,21),(17,19),(19,17))
        for a in ("eye-left-down-1","eye-left-down-2"):
            for b in ("eye-left-up-1","eye-left-up-2"):
                self.relate("connect",a,b)
        self.add_arc("eye-right-top",(27,18),(33,18),radius_x=3)
        self.add_arc("eye-right-bottom",(33,18),(27,18),radius_x=3)
        self.add_contour("eye-right","eye-right-top","eye-right-bottom",closed=True)
        self.add_line("grin-left",(14,30),(20,30))
        self.add_line("tongue-left",(20,30),(20,31))
        self.add_arc("tongue-tip",(20,31),(28,31),radius_x=4,sweep=False)
        self.add_line("tongue-right",(28,31),(28,29))
        self.add_line("grin-right",(28,29),(34,30))
        self.add_contour("grin-and-tongue","grin-left","tongue-left","tongue-tip","tongue-right","grin-right")
