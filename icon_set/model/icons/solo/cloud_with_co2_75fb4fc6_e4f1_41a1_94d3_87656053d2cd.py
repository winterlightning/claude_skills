"""An open cloud canopy above the text CO2.
Symbol plan: cloud: coherent lobed canopy; hand-authored C, O and lowered 2.
Reduction: None; all three text characters retained.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='75fb4fc6-e4f1-41a1-94d3-87656053d2cd'
SOURCE_PATH='icon_set/work/todo-references/cloud with co2_75fb4fc6-e4f1-41a1-94d3-87656053d2cd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cloud-with-co2'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('cloud', 'with', 'co2')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('cloud-left',(4,20),(8,16),radius_x=4)
        self.add_line('shoulder-left',(8,16),(16,16))
        self.add_arc('cloud-top',(16,16),(32,16),radius_x=8)
        self.add_line('shoulder-right',(32,16),(40,16))
        self.add_arc('cloud-right',(40,16),(44,20),radius_x=4)
        self.add_contour('cloud','cloud-left','shoulder-left','cloud-top','shoulder-right','cloud-right')
        self.add_bezier('c',(11,29),((7,27),(4,29),(4,34)),((4,39),(7,41),(11,39)))
        self.rounded('o',20,28,28,40,4)
        self.add_bezier('two-top',(37,32),((37,28),(44,28),(44,32)))
        self.add_polyline('two-base',(44,32),(37,40),(44,40));self.relate('connect','two-top','two-base')

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

