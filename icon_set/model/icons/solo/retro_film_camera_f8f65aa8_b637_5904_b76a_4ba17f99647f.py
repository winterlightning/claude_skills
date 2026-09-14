"""A retro still camera with a left viewfinder, short slot and right lens. Wide envelope fits its body. Lucide camera informs tangent round corners and lens construction. Controls are simplified but the raised left block and top hump remain; lens placement is deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8f65aa8-b637-5904-b76a-4ba17f99647f'
SOURCE_PATH = 'pictographic-primitives/photography/photography equipment retro film_f8f65aa8-b637-5904-b76a-4ba17f99647f.svg'
AUTHOR = 'gpt-6'

class RetroFilmCamera(Solo48):
    icon_id = 'retro-film-camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('camera', 'retro', 'film camera', 'vintage', 'photo', 'photography', 'lens', 'analog')

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

        segments('housing',(8,16),(8,8),(16,8),(16,16),(20,16),(24,8),(32,8),(36,16),(40,16))
        arc('tr',(40,16),(44,20),4);line('right',(44,20),(44,36));arc('br',(44,36),(40,40),4)
        line('bottom',(40,40),(8,40));arc('bl',(8,40),(4,36),4);line('left',(4,36),(4,20));arc('tl',(4,20),(8,16),4)
        contour('body',*[f'housing-{j}' for j in range(1,9)],'tr','right','br','bottom','bl','left','tl',closed=True)
        circle('lens',28,27,4)
        line('slot',(13,26),(15,26))
