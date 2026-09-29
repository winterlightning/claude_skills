"""cluster.
The lower branches hit the sides of the nodes and the vertical trunk was too short. Restore a balanced three-node Y with radial joins and equal circles.
Lucide network: repeated node dimensions and explicit trunk/branch attachments.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'db5443e9-3ef0-5724-b357-1ff8c8cb3b7b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cluster/20260928T164721Z-thuan-mac/reference/cluster_db5443e9-3ef0-5724-b357-1ff8c8cb3b7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cluster'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    aliases = ()
    keywords = ('cluster',)

    def build(self):

        def path(n,start,*commands,closed=False):
            pt=start; members=[]
            for i,c in enumerate(commands):
                mid=f'{n}-{i}'
                if c[0]=='L': self.add_line(mid,pt,c[1]); end=c[1]
                elif c[0]=='A':
                    _,end,rx,ry,sweep=c
                    self.add_arc(mid,pt,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif c[0]=='C':
                    _,a,b,end=c; self.add_bezier(mid,pt,(a,b,end))
                pt=end;members.append(mid)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def box(n,l,t,r,b,rad=2):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def bez(n,start,*s): self.add_bezier(n,start,*s)
        def join(a,b): self.relate('connect',a,b)
        circle('top',24,13,7)
        # 3-4-5 integer triangle defines exact radial lower-node junctions.
        path('left-node',(6,35),('A',(13,28),7,7,True),('A',(20,35),7,7,True),('A',(13,42),7,7,True),('A',(6,35),7,7,True),closed=True)
        path('right-node',(28,35),('A',(35,28),7,7,True),('A',(42,35),7,7,True),('A',(35,42),7,7,True),('A',(28,35),7,7,True),closed=True)
        line('trunk',(24,20),(24,26));line('left-branch',(24,26),(18,30));line('right-branch',(24,26),(30,30))
        join('top','trunk');join('trunk','left-branch');join('trunk','right-branch');join('left-branch','right-branch');join('left-node','left-branch');join('right-node','right-branch')
