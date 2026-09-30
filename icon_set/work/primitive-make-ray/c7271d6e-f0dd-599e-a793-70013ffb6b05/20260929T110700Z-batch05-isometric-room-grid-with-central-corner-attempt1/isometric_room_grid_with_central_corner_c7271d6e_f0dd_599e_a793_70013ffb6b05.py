'Terminated the central wall corner at the floor junction and rebuilt the separate floor plane under the wall grid.\nOriginal/current comparison: The rejected centerline extends to the bottom vertex, making the room look like a fishbone instead of two walls and a floor.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: Lucide box original and atomic-debug: coherent isometric edge graph and shared junctions. Source room interpretation reverses the box depth and preserves the floor.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c7271d6e-f0dd-599e-a793-70013ffb6b05'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__isometric-room-grid-with-central-corner/20260929T110700Z-thuan-mac/reference/grid perspective_c7271d6e-f0dd-599e-a793-70013ffb6b05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'isometric-room-grid-with-central-corner'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('isometric', 'room', 'grid', 'with', 'central', 'corner')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        nodes={'T':(24,4),'L':(8,14),'R':(40,14),'BL':(8,34),'BR':(40,34),'B':(24,44),'C':(24,28),'M':(24,14),'LM':(8,24),'RM':(40,24)}
        edges=[('T','L'),('T','R'),('L','LM'),('LM','BL'),('R','RM'),('RM','BR'),('BL','B'),('B','BR'),('T','M'),('M','C'),('BL','C'),('C','BR'),('LM','M'),('M','RM')]
        for i,(a,b) in enumerate(edges):line('edge-'+str(i),nodes[a],nodes[b])
        for i,(a,b) in enumerate(edges):
            for j,(c,d) in enumerate(edges[:i]):
                if {a,b}&{c,d}:join('edge-'+str(i),'edge-'+str(j))
