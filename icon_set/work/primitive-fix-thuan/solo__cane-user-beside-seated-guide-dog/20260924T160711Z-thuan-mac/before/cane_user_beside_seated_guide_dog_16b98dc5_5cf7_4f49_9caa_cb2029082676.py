"""A walking cane user with a seated guide dog on the left.
HRECT_L reaches (4,8)-(44,40). Human head r4 at (26,12), vertical torso
axis and neck (28,24) give exact 8 centerline gap. Human reference supplies
round head and single-stroke limbs; source supplies cane and companion.
Lucide dog inspected: frontal face unsuited to this small seated profile.
Omit facial details, fingers and collar. Dog owns one open profile contour.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID="16b98dc5-5cf7-4f49-9caa-cb2029082676"
SOURCE_PATH="pictographic-primitives/_uncategorized_15/dog for blind_16b98dc5-5cf7-4f49-9caa-cb2029082676.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id="cane-user-beside-seated-guide-dog"
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="Uncategorized"
    aliases=("Visually Impaired Person with Guide Dog",)
    keywords=("person","cane","guide","dog","walking","assistance","mobility")
    def build(self):
        self.add_arc("head-top",(24,12),(32,12),radius_x=4)
        self.add_arc("head-bottom",(32,12),(24,12),radius_x=4)
        self.add_contour("head","head-top","head-bottom",closed=True)
        self.add_line("torso",(28,24),(28,30))
        self.add_polyline("legs",(26,40),(28,30),(34,40))
        self.add_polyline("arm",(28,24),(32,28),(38,28))
        self.add_line("cane",(38,28),(44,40))
        self.relate("connect","torso","legs")
        self.relate("connect","torso","arm")
        self.relate("connect","arm","cane")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")
        self.add_bezier("dog-back",(4,40),((4,34),(6,34),(6,30)))
        self.add_line("dog-ear",(6,30),(6,24))
        pts=[(6,24),(14,24),(18,28),(14,32),(14,40)]
        for i,(a,b) in enumerate(zip(pts,pts[1:]),1): self.add_line(f"dog-face-{i}",a,b)
        self.add_contour("dog","dog-back","dog-ear","dog-face-1","dog-face-2","dog-face-3","dog-face-4")
