"""A tilted studio umbrella reflector on a three-foot stand. Vertical envelope gives the stand room. Lucide umbrella informs a smooth canopy arc; tilt follows the supplied reflector. Fine ribs and scallops reduce to one canopy and a central support."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2a6e813-bfdc-47ef-aa7e-d1d6e4892942'
SOURCE_PATH = 'pictographic-primitives/photography/light umbrella_e2a6e813-bfdc-47ef-aa7e-d1d6e4892942.svg'
AUTHOR = 'gpt-6'

class UmbrellaLightStand(Solo48):
    icon_id = 'umbrella-light-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('umbrella light', 'reflector', 'studio', 'lighting', 'stand', 'photography', 'softbox', 'equipment')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8]
                if j%2:arc(n+str(j),a,z,rad)
                else:line(n+str(j),a,z)
            contour(n,*[n+str(j) for j in range(8)],closed=True)

        arc('canopy',(8,24),(40,8),20,sweep=True)
        poly('underside',(40,8),(24,16),(8,24));connect('canopy','underside')
        line('strut',(24,16),(36,28));connect('strut','underside')
        poly('pole',(28,20),(28,36),(28,44));connect('pole','strut')
        for x in (16,40):line('foot-'+str(x),(28,36),(x,44));connect('foot-'+str(x),'pole')
        connect('foot-16','foot-40')
