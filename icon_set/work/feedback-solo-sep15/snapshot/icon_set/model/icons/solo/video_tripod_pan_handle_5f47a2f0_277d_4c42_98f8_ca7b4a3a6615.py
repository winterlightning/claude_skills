"""A video tripod with a capsule head, right-angled pan handle and three legs. Vertical envelope fits the support. Lucide rectangle-horizontal informs rounded head construction; source defines the diagonal handle. Crossbar retained; small head mechanisms omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f47a2f0-277d-4c42-98f8-ca7b4a3a6615'
SOURCE_PATH = 'pictographic-primitives/photography/tripod_5f47a2f0-277d-4c42-98f8-ca7b4a3a6615.svg'
AUTHOR = 'gpt-6'

class VideoTripodPanHandle(Solo48):
    icon_id = 'video-tripod-pan-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('tripod', 'video tripod', 'pan handle', 'stand', 'camera', 'filming', 'photography', 'equipment')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
            for j,p in enumerate(pts):arc(n+'-'+str(j),p,pts[(j+1)%4],r)
            contour(n,*[n+'-'+str(j) for j in range(4)],closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8]
                if j%2:arc(n+str(j),a,z,rad)
                else:line(n+str(j),a,z)
            contour(n,*[n+str(j) for j in range(8)],closed=True)

        line('head-top',(20,4),(28,4));arc('head-tr',(28,4),(32,8),4);arc('head-br',(32,8),(28,12),4)
        segments('head-bottom',(28,12),(24,12),(20,12));arc('head-left',(20,12),(20,4),4)
        contour('head','head-top','head-tr','head-br','head-bottom-1','head-bottom-2','head-left',closed=True)
        line('pan-handle',(32,8),(40,18));connect('pan-handle','head')
        line('column',(24,12),(24,24));connect('column','head')
        poly('crossbar',(16,24),(24,24),(32,24));connect('crossbar','column')
        for j,x in enumerate((8,24,40)):
            line('leg-'+str(j),(24,24),(x,44));connect('leg-'+str(j),'column')
        for a,b in ((0,1),(1,2),(0,2)):connect('leg-'+str(a),'leg-'+str(b))
        for j in range(3):connect('crossbar','leg-'+str(j))
