"""A studio spotlight with four barn-door flaps and a pole foot. Vertical envelope preserves the stand. Lucide projector informs the round lamp; the source supplies the four trapezoid flaps. Shared flap corners and lamp endpoints are explicit; no barn doors are dropped."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3b88a64-8303-56f9-ae7f-40decb860b30'
SOURCE_PATH = 'pictographic-primitives/photography/photography equipment light_c3b88a64-8303-56f9-ae7f-40decb860b30.svg'
AUTHOR = 'gpt-6'

class StudioSpotlightBarnDoors(Solo48):
    icon_id = 'studio-spotlight-barn-doors'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('spotlight', 'studio light', 'barn doors', 'lighting', 'stand', 'photography', 'film', 'equipment')

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

        pts=[(16,12),(32,12),(32,24),(16,24)]
        for j,p in enumerate(pts):arc('rim-'+str(j),p,pts[(j+1)%4],10)
        contour('lamp',*[f'rim-{j}' for j in range(4)],closed=True)
        poly('top-door',(16,12),(12,4),(36,4),(32,12))
        poly('right-door',(32,12),(40,8),(40,28),(32,24))
        poly('bottom-door',(32,24),(36,32),(24,32),(12,32),(16,24))
        poly('left-door',(16,24),(8,28),(8,8),(16,12))
        doors=('top-door','right-door','bottom-door','left-door')
        for j,n in enumerate(doors):connect(n,'lamp');connect(n,doors[(j+1)%4])
        line('pole',(24,32),(24,44));connect('pole','bottom-door')
        poly('foot',(14,44),(24,44),(34,44));connect('foot','pole')
