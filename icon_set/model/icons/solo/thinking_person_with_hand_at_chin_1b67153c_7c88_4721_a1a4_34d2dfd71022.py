"""A circular-headed portrait with one hand raised to its chin.
VRECT_L (8,4)-(40,44). human_ref/user.svg supplies circular head and broad
rounded shoulders; Lucide user-round confirms coherent circular construction.
Head (24,12), r8: bottom20, bodytop24, zero visible head/body gap.
The right arm is deliberately asymmetric; simplify fingers to one bent stroke.
Shared body crown (24,24) owns the raised hand. Open bottom avoids a trapped pocket.
"""
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from ...keyshapes import Keyshape
SOURCE_ICON_ID="1b67153c-7c88-4721-a1a4-34d2dfd71022"
SOURCE_PATH="pictographic-primitives/_uncategorized_15/doubter_1b67153c-7c88-4721-a1a4-34d2dfd71022.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id="thinking-person-with-hand-at-chin"
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="avatars"
    aliases=("Thinking and Pondering Person",)
    keywords=("person","thinking","chin","hand","pose","portrait","pondering")
    def build(self):
        cx,cy,r=24,12,8
        self.add_arc("head-top",(16,12),(32,12),radius_x=r)
        self.add_arc("head-bottom",(32,12),(16,12),radius_x=r)
        self.add_contour("head","head-top","head-bottom",closed=True)
        top=cy+r+HEAD_BODY_CENTERLINE_GAP
        self.add_line("body-left-side",(8,44),(8,40))
        self.add_arc("body-top",(8,40),(24,top),radius_x=16)
        self.add_contour("body","body-left-side","body-top")
        self.add_bezier("body-raised-arm",(24,top),((24,30),(28,40),(32,44)),((40,44),(40,40),(40,36)),((40,30),(37,26),(34,26)))
        self.relate("connect","head","body")
        self.relate("connect","head","body-raised-arm")
        self.relate("connect","body","body-raised-arm")
