"""Two equal toothed gears on a rising diagonal.
Symbol plan: cog: repeated radial teeth and circular hubs, generated from shared quarter geometry.
Reduction: Eight teeth per gear reduced to four broad teeth to open tooth valleys; both hubs retained.
Keyshape: SQUARE; model supplies exact ink extremes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='b484255b-2a40-40d1-9943-7e27cfb9f399'
SOURCE_PATH='icon_set/work/todo-references/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cog-double'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('cog', 'double')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        quarter=[(-4,-9),(4,-9),(4,-4),(9,-4)]
        for i,(cx,cy) in enumerate(((15,33),(33,15))):
            pts=[]
            for turn in range(4):
                for x,y in quarter:
                    for _ in range(turn):x,y=-y,x
                    pts.append((cx+x,cy+y))
            self.add_polyline(f'gear-{i}',*pts,closed=True)
            self.circle(f'hub-{i}',cx,cy,3)

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

