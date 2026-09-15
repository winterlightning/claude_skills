"""Vertical two-frame film strip; inset frame outlines replaced by shared rails, with four open sprocket cells on each side."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '137235f7-8629-4162-9739-79c63dd5b41a'
SOURCE_PATH = 'pictographic-primitives/movies/movies film_137235f7-8629-4162-9739-79c63dd5b41a.svg'
AUTHOR = 'gpt-6'

class TwoFrameFilmStrip(Solo48):
    icon_id = 'two-frame-film-strip'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/media'
    aliases = ()
    keywords = ('film', 'strip', 'frames', 'cinema', 'movie', 'perforations')

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
        # Shared rails and side cells form two picture windows and four sprocket holes per side.
        box(8,4,40,44,rad=4,ys=(14,24,34),xs=(16,32))
        for x in (16,32):
            self.add_polyline(f'rail-{x}',(x,4),(x,14),(x,24),(x,34),(x,44))
            self.relate('connect',f'rail-{x}','body')
        for y in (14,24,34):
            for side,l,r in [('left',8,16),('right',32,40)]:
                n=f'sprocket-{side}-{y}';line(n,(l,y),(r,y))
                self.relate('connect',n,'body');self.relate('connect',n,f'rail-{16 if side=="left" else 32}')
        line('frame-divider',(16,24),(32,24))
        for x in (16,32):self.relate('connect','frame-divider',f'rail-{x}')
