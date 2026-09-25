"""Phone snapped into two jagged pieces with lower bezel; detached impact strokes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0a85746-972b-4441-acf2-c38ad5f44ea6'
SOURCE_PATH = 'pictographic-primitives/phones/phone broken_b0a85746-972b-4441-acf2-c38ad5f44ea6.svg'
AUTHOR = 'gpt-6'

class BrokenSmartphoneWithLowerBezel(Solo48):
    icon_id = 'broken-smartphone-with-lower-bezel'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('phone', 'broken', 'damage', 'crack', 'smartphone', 'repair')

    def build(self):
        def line(n, a, b): self.add_line(n, a, b)
        def segments(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):line(f"{n}-{i}",a,b)
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
        line('top',(12,4),(36,4));arc('tr',(36,4),(40,8),4)
        segments('upper-break',(40,8),(40,16),(28,12),(20,16),(8,16),(8,8))
        arc('tl',(8,8),(12,4),4)
        self.add_contour('upper','top','tr',*[f'upper-break-{i}' for i in range(1,6)],'tl',closed=True)
        segments('lower-break',(8,40),(8,34),(8,26),(20,26),(28,22),(40,26),(40,34),(40,40))
        arc('br',(40,40),(36,44),4);line('bottom',(36,44),(12,44));arc('bl',(12,44),(8,40),4)
        self.add_contour('lower',*[f'lower-break-{i}' for i in range(1,8)],'br','bottom','bl',closed=True)
        line('bezel',(8,34),(40,34));self.relate('connect','bezel','lower')
