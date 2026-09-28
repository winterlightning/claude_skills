"""A square frame holds a woman with parted hair and rounded shoulders.
Symbol plan: Square frame; circular head and symmetric hair; cropped shoulder arch with exact 8-unit centerline gap: 33-(20+5)=8.
Keyshape visible bounds: (4, 4, 44, 44).
Construction references: Shared human_ref/user.svg: circular head and smooth shoulders; Lucide square-user-round: frame and cropped shoulders; supplied woman reference: parted hair and tails..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1'
SOURCE_PATH = 'pictographic-primitives/other/square woman_7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'square-woman'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('square', 'woman')
    def build(self):
        self.box('frame',6,6,42,42,2)
        cx,cy,r=24,20,5
        self.circle('head',cx,cy,r)
        # Parted hair meets the circular outline at its left/right extrema.
        self.add_bezier('hair-part',(19,20),((21,20),(23,18),(24,17)),((25,18),(27,20),(29,20)))
        self.relate('connect','head','hair-part')
        for side in [-1,1]:
            self.add_bezier(f'hair-tail-{side}',(cx+side*r,cy),((cx+side*r,22),(cx+side*6,25),(cx+side*7,26)))
            self.relate('connect','head',f'hair-tail-{side}')
            self.relate('connect','hair-part',f'hair-tail-{side}')
        self.add_arc('shoulder-left',(15,42),(24,33),radius_x=9)
        self.add_arc('shoulder-right',(24,33),(33,42),radius_x=9)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.relate('connect','frame','shoulders')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)
