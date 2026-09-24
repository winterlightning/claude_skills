"""Two coworkers below a disconnected plug and socket joined by an outer cord.
Symbol plan: plug: cap and paired prongs; human_ref/user.svg: equivalent circular heads and shoulders.
Reduction: Socket holes reduced from two to one; closed shoulder bases omitted for clear bust silhouettes.
Keyshape: SQUARE; model supplies exact ink extremes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4'
SOURCE_PATH='icon_set/work/todo-references/co working space plug users_2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='co-working-space-plug-users'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('co', 'working', 'space', 'plug', 'users')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        for i,cx in enumerate((13,35)):
            self.circle(f'head-{i}',cx,28,4)
            self.add_arc(f'shoulders-{i}',(cx-7,42),(cx+7,42),radius_x=7,radius_y=2)
        # Head bottom32, shoulder apex40: exact8 centerline /4 ink units.
        self.rounded('plug',10,6,20,18,2,breaks={2:[(20,8),(20,16)],6:[(10,12)]})
        self.rounded('socket',32,6,42,18,3,breaks={2:[(42,12)]})
        for i,y in enumerate((8,16)):
            self.add_line(f'pin-{i}',(20,y),(24,y));self.relate('connect',f'pin-{i}','plug')
        self.add_dot('socket-hole',(37,12))
        self.add_polyline('cord-left',(10,12),(6,12),(6,24),(13,24));self.relate('connect','cord-left','plug');self.relate('connect','cord-left','head-0')
        self.add_polyline('cord-right',(42,12),(42,24),(35,24));self.relate('connect','cord-right','socket');self.relate('connect','cord-right','head-1')

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

