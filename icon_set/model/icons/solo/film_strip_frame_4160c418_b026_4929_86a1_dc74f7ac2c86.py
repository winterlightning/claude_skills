"""A rounded film-strip frame with three sprocket openings above and below its image window. Square envelope; Lucide film informs rounded corners and connected perforation rails. Detached dashes become open rectangular sprockets. All three openings in each band are retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4160c418-b026-4929-86a1-dc74f7ac2c86'
SOURCE_PATH = 'pictographic-primitives/photography/film_4160c418-b026-4929-86a1-dc74f7ac2c86.svg'
AUTHOR = 'gpt-6'

class FilmStripFrame(Solo48):
    icon_id = 'film-strip-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('film', 'film strip', 'frame', 'movie', 'photography', 'negative', 'cinema', 'reel')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)

        # Three perforations in each band, derived from a shared 12-unit pitch.
        xs=(6,18,30,42)
        for y in (6,14,34,42):
            ends=(10,18,30,38) if y in (6,42) else xs
            poly('rail-'+str(y),*[(x,y) for x in ends])
        for x in (6,42):
            poly('edge-'+str(x),(x,10),(x,14),(x,34),(x,38))
        for n,a,b in [('tl',(6,10),(10,6)),('tr',(38,6),(42,10)),('br',(42,38),(38,42)),('bl',(10,42),(6,38))]:
            arc(n,a,b,4)
            for y in ((6,) if n in ('tl','tr') else (42,)):connect(n,'rail-'+str(y))
            connect(n,'edge-'+str(6 if n in ('tl','bl') else 42))
        for y in (14,34):
            for x in (6,42):connect('rail-'+str(y),'edge-'+str(x))
        for y1,y2 in ((6,14),(34,42)):
            for x in (18,30):
                name=f'perforation-{x}-{y1}';line(name,(x,y1),(x,y2))
                connect(name,'rail-'+str(y1));connect(name,'rail-'+str(y2))
