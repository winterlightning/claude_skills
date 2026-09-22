"""Masked person with a broad band and shallow nose bridge. VRECT_L fits circular face center24,19 radius15 and curved shoulders. Jaw34 and shoulder38 leave zero ink gap. Source provides mask; human_ref/user.svg provides round head and open shoulders; Lucide venetian-mask informs paired eyes and bridge. Eye slits reduced to dots; separate frown and neck seam omitted for readable spacing. Repaired existing draft."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='981592fe-af1b-4959-b91c-c4a4f98b6eee'
SOURCE_PATH='pictographic-primitives/_uncategorized_26/man thief 2_981592fe-af1b-4959-b91c-c4a4f98b6eee.svg'
AUTHOR="gpt-6-astra"
class Drawing(Solo48):
    icon_id='masked-person-with-frowning-mouth'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="avatars"
    human_construction="bust"
    aliases=("Man Wearing Thief Mask",)
    keywords=("mask","thief","portrait","disguise")
    def build(self):
        cx,cy,r=24,19,15
        points=[(cx-12,cy-9),(cx,cy-r),(cx+12,cy-9),(cx+r,cy),
                (cx+12,cy+9),(cx,cy+r),(cx-12,cy+9),(cx-r,cy),(cx-12,cy-9)]
        names = ["face" if i == 4 else "jaw" if i == 5 else f"face-{i}" for i in range(8)]
        for i in range(8):
            self.add_arc(names[i],points[i],points[i+1],radius_x=r)
        self.add_contour('head',*names,closed=True)
        self.add_line('mask-top',(12,10),(36,10))
        self.add_bezier('mask-bottom',(12,28),((18,28),(20,28),(24,27)),((28,28),(30,28),(36,28)))
        self.relate('connect','mask-top','head')
        self.relate('connect','mask-bottom','head')
        for x in [18,30]:
            self.add_dot('eye-'+str(x),(x,19))
        self.add_arc('body-left-shoulder',(8,44),(14,38),radius_x=6)
        self.add_line('body-top',(14,38),(34,38))
        self.add_arc('body-right-shoulder',(34,38),(40,44),radius_x=6)
        self.add_contour('body','body-left-shoulder','body-top','body-right-shoulder')
        self.relate('connect','head','body')
