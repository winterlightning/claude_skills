"""Film reel with a descending right-hand strip and upturned curl; six radial marks reduced to four dots and the tiny hub omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb8ed868-dc9b-5a26-834a-776a1895d45e'
SOURCE_PATH = 'pictographic-primitives/movies/movies reel_eb8ed868-dc9b-5a26-834a-776a1895d45e.svg'
AUTHOR = 'gpt-6'

class FilmReelWithHangingTail(Solo48):
    icon_id = 'film-reel-with-hanging-tail'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/media'
    aliases = ()
    keywords = ('film', 'reel', 'spool', 'cinema', 'movie', 'tail')

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
        circle('reel',20,24,16)
        for name,p in [('top',(20,17)),('right',(27,24)),('bottom',(20,31)),('left',(13,24))]:self.add_dot(f'radial-{name}',p)
        line('hanging-film',(36,24),(36,36));arc('tail-curl',(36,36),(44,36),4,False)
        line('tail-end',(44,36),(44,32))
        self.add_contour('tail','hanging-film','tail-curl','tail-end');self.relate('connect','tail','reel')
