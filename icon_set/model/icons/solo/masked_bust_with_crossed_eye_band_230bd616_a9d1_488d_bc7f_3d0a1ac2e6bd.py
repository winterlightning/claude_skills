"""Masked bust with crossing eye-band boundaries. VRECT_L budgets circular head center (24,18), radius14, and broad circular shoulders. Jaw32 and shoulder36 give zero ink gap (4 centerline). Source preserves crossed band; human_ref/user.svg supplies open round shoulders; Lucide venetian-mask informs paired lobes. Frown and neck seam omitted to avoid crowded face. Mask crossings are not declared joins."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='230bd616-a9d1-488d-bc7f-3d0a1ac2e6bd'
SOURCE_PATH='pictographic-primitives/_uncategorized_26/man thief 1_230bd616-a9d1-488d-bc7f-3d0a1ac2e6bd.svg'
AUTHOR="gpt-6-astra"
class Drawing(Solo48):
    icon_id='masked-bust-with-crossed-eye-band'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="avatars"
    human_construction="bust"
    aliases=("Masked Thief Avatar",)
    keywords=("mask","thief","portrait","disguise")
    def build(self):
        cx,cy,r=24,18,14
        points=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        names = ["face" if i == 2 else "jaw" if i == 3 else f"face-{i}" for i in range(4)]
        for i in range(4):
            self.add_arc(names[i],points[i],points[i+1],radius_x=r)
        self.add_contour('head',*names,closed=True)
        self.add_bezier('mask-rising',(10,18),((15,28),(19,28),(24,18)),((29,8),(33,8),(38,18)))
        self.add_bezier('mask-falling',(10,18),((15,8),(19,8),(24,18)),((29,28),(33,28),(38,18)))
        self.relate('connect','mask-rising','head')
        self.relate('connect','mask-falling','head')
        self.add_arc('body-left-shoulder',(8,44),(16,36),radius_x=8)
        self.add_line('body-top',(16,36),(32,36))
        self.add_arc('body-right-shoulder',(32,36),(40,44),radius_x=8)
        self.add_contour('body','body-left-shoulder','body-top','body-right-shoulder')
        self.relate('connect','head','body')
