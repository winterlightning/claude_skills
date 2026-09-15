"""Circular reel with four round opening marks and a loose rightward film tail; opening outlines reduced to dots to keep all four."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4fb486e-90a1-5668-9337-0790c0a1707d'
SOURCE_PATH = 'pictographic-primitives/movies/movies reel_d4fb486e-90a1-5668-9337-0790c0a1707d.svg'
AUTHOR = 'gpt-6'

class FourHoleFilmReel(Solo48):
    icon_id = 'four-hole-film-reel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/media'
    aliases = ()
    keywords = ('film', 'reel', 'cinema', 'movie', 'spool', 'roll')

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
        # Four equal round openings are reduced to dots around the shared reel center.
        circle('reel',22,22,16)
        for name,p in [('top',(22,15)),('right',(29,22)),('bottom',(22,29)),('left',(15,22))]:self.add_dot(f'opening-{name}',p)
        line('loose-film',(22,38),(38,38));arc('film-tip',(38,38),(42,42),4)
        self.add_contour('tail','loose-film','film-tip');self.relate('connect','tail','reel')
