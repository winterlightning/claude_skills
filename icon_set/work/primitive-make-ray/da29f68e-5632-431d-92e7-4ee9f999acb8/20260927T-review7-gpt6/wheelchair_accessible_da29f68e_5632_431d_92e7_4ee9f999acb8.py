"""A seated person reaches forward from a wheelchair seat above one large clean wheel. Human proportions use icon_set/references/human_ref/full_body_ref.png."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="da29f68e-5632-431d-92e7-4ee9f999acb8"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__wheelchair-accessible/20260926T171117Z-thuan-mac-1/reference/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg"
AUTHOR="gpt-6"
class WheelchairAccessible(Solo48):
    icon_id="wheelchair-accessible"
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="symbol"
    aliases=()
    keywords=("wheelchair", "accessibility", "mobility", "inclusive")
    def build(self):
        pts=((16,22),(26,32),(16,42),(6,32),(16,22));members=[]
        for n,(a,b) in enumerate(zip(pts,pts[1:])):
            name=f"wheel-{n}";self.add_arc(name,a,b,radius_x=10);members.append(name)
        self.add_contour("wheel",*members,closed=True)
        self.add_arc("head-upper",(30,10),(38,10),radius_x=4)
        self.add_arc("head-lower",(38,10),(30,10),radius_x=4)
        self.add_contour("head","head-upper","head-lower",closed=True)
        self.add_line("torso",(34,22),(34,32))
        self.add_line("seat",(26,32),(34,32))
        self.add_line("leg",(34,32),(40,40))
        self.add_line("foot",(40,40),(42,40))
        self.add_line("arm",(34,23),(42,20))
        self.relate("connect","seat","wheel")
        self.relate("connect","torso","seat")
        self.relate("connect","torso","leg")
        self.relate("connect","leg","foot")
        self.relate("connect","arm","torso")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")
