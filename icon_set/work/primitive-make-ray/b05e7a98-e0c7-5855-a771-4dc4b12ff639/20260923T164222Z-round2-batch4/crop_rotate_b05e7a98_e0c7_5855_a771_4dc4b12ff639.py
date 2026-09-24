"""Crossing crop corners with opposing rotation arrows.
Symbol plan: crop: shared crossing nodes; rotate-ccw: quarter arcs with compact corner arrowheads.
Reduction: Chevron arrowheads changed to right-angle arrowheads; both rotation arrows retained.
Keyshape: SQUARE; model supplies exact ink extremes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='b05e7a98-e0c7-5855-a771-4dc4b12ff639'
SOURCE_PATH='icon_set/work/todo-references/crop rotate_b05e7a98-e0c7-5855-a771-4dc4b12ff639.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='crop-rotate'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('crop', 'rotate')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('crop-left',(18,6),(18,18),(18,30),(30,30),(42,30))
        self.add_polyline('crop-right',(6,18),(18,18),(30,18),(30,30),(30,42));self.relate('connect','crop-left','crop-right')
        self.add_arc('rotate-top',(42,18),(30,6),radius_x=12,sweep=False)
        self.add_polyline('arrow-top',(34,6),(30,6),(30,10));self.relate('connect','rotate-top','arrow-top')
        self.add_arc('rotate-bottom',(6,30),(18,42),radius_x=12,sweep=False)
        self.add_polyline('arrow-bottom',(14,42),(18,42),(18,38));self.relate('connect','rotate-bottom','arrow-bottom')

    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(pts,pts[1:])):
            if i%2:
                m=f'{name}-{i}';self.add_arc(m,a,z,radius_x=rad);members.append(m)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end:continue
                    m=f'{name}-{i}-{j}';self.add_line(m,start,end);members.append(m)
        self.add_contour(name,*members,closed=True)

