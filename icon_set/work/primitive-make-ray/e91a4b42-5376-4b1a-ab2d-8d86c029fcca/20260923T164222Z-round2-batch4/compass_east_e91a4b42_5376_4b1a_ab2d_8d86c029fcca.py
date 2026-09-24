"""A circular east compass badge followed by a right arrow.
Symbol plan: compass: circular badge; hand-authored E and concave directional arrow.
Reduction: None.
Keyshape: HRECT_M; model supplies exact ink extremes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='e91a4b42-5376-4b1a-ab2d-8d86c029fcca'
SOURCE_PATH='icon_set/work/todo-references/compass east_e91a4b42-5376-4b1a-ab2d-8d86c029fcca.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='compass-east'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('compass', 'east')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('badge',17,24,13)
        self.add_polyline('e',(20,16),(13,16),(13,24),(13,32),(20,32))
        self.add_line('e-mid',(13,24),(19,24));self.relate('connect','e','e-mid')
        self.add_polyline('arrow',(36,10),(44,24),(36,38),(39,24),closed=True)

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

