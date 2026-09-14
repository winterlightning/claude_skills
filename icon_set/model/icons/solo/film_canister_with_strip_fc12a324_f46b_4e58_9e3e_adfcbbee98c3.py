"""An upright film canister with flanged rims and a stepped film leader pulled right. Wide envelope reserves space for the leader. Lucide film informs the structural film mark. Cap thickness reduces to strokes, and perforation rows reduce to one clear sprocket mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc12a324-f46b-4e58-9e3e-adfcbbee98c3'
SOURCE_PATH = 'pictographic-primitives/photography/retro film_fc12a324-f46b-4e58-9e3e-adfcbbee98c3.svg'
AUTHOR = 'gpt-6'

class FilmCanisterWithStrip(Solo48):
    icon_id = 'film-canister-with-strip'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('film', 'canister', 'roll', '35mm', 'retro', 'analog', 'photography', 'negative')

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

        poly('top-rim',(4,8),(8,8),(24,8),(28,8))
        poly('bottom-rim',(4,40),(8,40),(24,40),(28,40))
        line('canister-left',(8,8),(8,40))
        poly('canister-right',(24,8),(24,16),(24,40))
        for n in ('canister-left','canister-right'):
            connect(n,'top-rim');connect(n,'bottom-rim')
        poly('film-leader',(24,16),(44,16),(44,32),(36,32),(36,40),(28,40));connect('film-leader','canister-right');connect('film-leader','bottom-rim')
        self.add_dot('sprocket',(34,24))
