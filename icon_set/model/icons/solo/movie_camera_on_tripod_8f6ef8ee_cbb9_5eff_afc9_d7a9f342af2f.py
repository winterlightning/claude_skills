"""Right-facing movie camera with raised handle, flared lens hood and three splayed tripod legs; minor equipment seams omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f6ef8ee-cbb9-5eff-afc9-d7a9f342af2f'
SOURCE_PATH = 'pictographic-primitives/movies/movies set equipment_8f6ef8ee-cbb9-5eff-afc9-d7a9f342af2f.svg'
AUTHOR = 'gpt-6'

class MovieCameraOnTripod(Solo48):
    icon_id = 'movie-camera-on-tripod'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'movies'
    aliases = ()
    keywords = ('camera', 'movie', 'film', 'tripod', 'lens', 'production')

    def build(self):
        def line(n, a, b): self.add_line(n, a, b)
        def arc(n, a, b, r, sweep=True):
            self.add_arc(n, a, b, radius_x=r, sweep=sweep)
        def circle(n, x, y, r):
            arc(n+'-top', (x,y+r), (x,y-r), r)
            arc(n+'-bottom', (x,y-r), (x,y+r), r)
            self.add_contour(n,n+'-top',n+'-bottom',closed=True)
        def box(l,t,r,b,rad=4,ys=(),xs=()):
            # Shared bounds and radius own all four tangent corners.
            members=[]
            def run(n,pts):
                for i,(a,z) in enumerate(zip(pts,pts[1:])):
                    name=f'{n}-{i}';line(name,a,z);members.append(name)
            def corner(n,a,z):
                arc(n,a,z,rad);members.append(n)
            run('top',[(l+rad,t)]+[(x,t) for x in sorted(xs)]+[(r-rad,t)])
            corner('top-right',(r-rad,t),(r,t+rad))
            run('right',[(r,t+rad)]+[(r,y) for y in sorted(ys)]+[(r,b-rad)])
            corner('bottom-right',(r,b-rad),(r-rad,b))
            run('bottom',[(r-rad,b)]+[(x,b) for x in sorted(xs,reverse=True)]+[(l+rad,b)])
            corner('bottom-left',(l+rad,b),(l,b-rad))
            run('left',[(l,b-rad)]+[(l,y) for y in sorted(ys,reverse=True)]+[(l,t+rad)])
            corner('top-left',(l,t+rad),(l+rad,t))
            self.add_contour('body',*members,closed=True)
        def seam(n,a,b):
            line(n,a,b)
            # Both receiver walls are split at this seam's endpoints.
            self.relate('connect',n,'body')
        box(6,14,30,28,rad=3,ys=(18,24),xs=(14,18,22))
        self.add_polyline('handle',(14,14),(14,6),(22,6),(22,14));self.relate('connect','handle','body')
        self.add_polyline('lens-hood',(30,18),(42,12),(42,30),(30,24));self.relate('connect','lens-hood','body')
        line('mount',(18,28),(18,34));line('center-leg',(18,34),(18,42))
        self.relate('connect','mount','body');self.relate('connect','center-leg','mount')
        for name,end in [('left',(8,42)),('right',(28,42))]:
            line(f'leg-{name}',(18,34),end)
            self.relate('connect',f'leg-{name}','mount');self.relate('connect',f'leg-{name}','center-leg')
        self.relate('connect','leg-left','leg-right')
