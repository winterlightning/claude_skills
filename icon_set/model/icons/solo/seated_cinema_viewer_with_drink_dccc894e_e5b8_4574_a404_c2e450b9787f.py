"""Reclining cinema viewer with cup, bent straw, chair and extended leg; background screen and duplicate leg contour omitted for clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dccc894e-e5b8-4574-a404-c2e450b9787f'
SOURCE_PATH = 'pictographic-primitives/movies/movies sit drink_dccc894e-e5b8-4574-a404-c2e450b9787f.svg'
AUTHOR = 'gpt-6'

class SeatedCinemaViewerWithDrink(Solo48):
    icon_id = 'seated-cinema-viewer-with-drink'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/media'
    aliases = ()
    keywords = ('cinema', 'viewer', 'seat', 'drink', 'screen', 'movie')

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
        # A side-view reclined figure, extended leg, chair and held drink form one scene.
        circle('head',32,10,4)
        self.add_polyline('cup',(6,16),(10,16),(14,16),(14,24),(6,24),closed=True)
        self.add_polyline('straw',(10,16),(10,10),(16,8));self.relate('connect','straw','cup')
        self.add_polyline('arm',(14,24),(24,24),(32,23));self.relate('connect','arm','cup')
        line('torso',(32,23),(28,32));self.relate('connect','torso','arm')
        self.add_polyline('chair',(42,20),(38,42),(22,42),(18,32),(20,32),(28,32),(34,32))
        self.relate('connect','chair','torso')
        self.add_polyline('leg',(28,32),(20,32),(6,38))
        self.relate('connect','leg','torso');self.relate('connect','leg','chair')
