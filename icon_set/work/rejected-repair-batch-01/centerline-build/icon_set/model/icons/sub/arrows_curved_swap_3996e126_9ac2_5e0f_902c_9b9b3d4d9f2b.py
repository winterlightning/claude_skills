"""Opposed swap arrows joined by a continuous winding shaft; routed to SUB32 as an operator."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3996e126-9ac2-5e0f-902c-9b9b3d4d9f2b'
SOURCE_PATH = 'pictographic-primitives/phones/phone swap_3996e126-9ac2-5e0f-902c-9b9b3d4d9f2b.svg'
AUTHOR = 'gpt-6'

class ArrowsCurvedSwap(Sub32):
    icon_id = 'arrows-curved-swap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/arrow'
    aliases = ()
    keywords = ('arrows', 'swap', 'exchange', 'curved', 'up', 'down')

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
        def segments(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):line(f'{n}-{i}',a,b)
        def ellipse(n,a,b,rx,ry,sweep=True):
            self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def compact_receiver():
            line('receiver-top',(16,6),(32,6));arc('receiver-r',(32,6),(42,16),10)
            segments('receiver-low',(42,16),(42,17),(34,17),(34,14),(24,14),(14,14),(14,17),(6,17),(6,16))
            arc('receiver-l',(6,16),(16,6),10)
            self.add_contour('receiver','receiver-top','receiver-r',*[f'receiver-low-{i}' for i in range(1,9)],'receiver-l',closed=True)
        # One winding shaft, with tangent half-circles and opposed tips.
        line('left-shaft',(6,22),(6,7));arc('upper-turn',(6,7),(16,7),5)
        line('middle',(16,7),(16,25));arc('lower-turn',(16,25),(26,25),5,False)
        line('right-shaft',(26,25),(26,10))
        self.add_contour('shaft','left-shaft','upper-turn','middle','lower-turn','right-shaft')
        self.add_polyline('down-tip',(2,18),(6,22),(10,18))
        self.add_polyline('up-tip',(22,14),(26,10),(30,14))
        self.relate('connect','down-tip','shaft');self.relate('connect','up-tip','shaft')
