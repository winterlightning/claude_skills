"""A skull with slanted eyes inside a circular badge.
Symbol plan: skull: domed head and narrowed open jaw; source dictates circular enclosure.
Reduction: Slanted eye strokes shortened for clearance.
Keyshape: CIRCLE; model supplies exact ink extremes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='0275d46c-9a52-48fb-9993-9a0c2a0a4b89'
SOURCE_PATH='icon_set/work/todo-references/circle skull 1_0275d46c-9a52-48fb-9993-9a0c2a0a4b89.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circle-skull-1'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('circle', 'skull', '1')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('ring',24,24,20)
        self.add_arc('dome',(13,23),(35,23),radius_x=11)
        self.add_bezier('right-cheek',(35,23),((35,28),(32,29),(32,30)))
        self.add_line('right-jaw',(32,30),(32,32))
        self.add_line('left-jaw',(16,32),(16,30))
        self.add_bezier('left-cheek',(16,30),((16,29),(13,28),(13,23)))
        self.add_contour('skull','left-jaw','left-cheek','dome','right-cheek','right-jaw')
        self.add_line('mouth',(24,32),(24,34))

        for side in (-1,1):self.add_line('eye-'+str(side),(24+side*5,23),(24+side*4,24))

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

