"""A Christmas postcard with a snowflake, divider, stamp and address rules.
Symbol plan: snowflake: branched axial strokes; source postcard layout.
Reduction: Two address rules reduced to one; all four snowflake branches retained.
Keyshape: HRECT_L; model supplies exact ink extremes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='6341f7cd-9be8-48da-9d1f-bb8141ad4804'
SOURCE_PATH='icon_set/work/todo-references/christmas postcard 2_6341f7cd-9be8-48da-9d1f-bb8141ad4804.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='christmas-postcard-2'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('christmas', 'postcard', '2')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.rounded('card',4,8,44,40,3)
        self.add_line('divider',(27,17),(27,31))
        self.add_polyline('flake-v',(16,17),(16,20),(16,24),(16,28),(16,31))
        self.add_polyline('flake-h',(9,24),(12,24),(16,24),(20,24),(23,24));self.relate('connect','flake-v','flake-h')
        for n,pts,parent in [('north',[(13,18),(16,20),(19,18)],'flake-v'),('south',[(13,30),(16,28),(19,30)],'flake-v'),('west',[(10,21),(12,24),(10,27)],'flake-h'),('east',[(22,21),(20,24),(22,27)],'flake-h')]:
            self.add_polyline(n,*pts);self.relate('connect',n,parent)
        self.circle('stamp',36,20,3)
        self.add_line('address',(33,32),(38,32))

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

