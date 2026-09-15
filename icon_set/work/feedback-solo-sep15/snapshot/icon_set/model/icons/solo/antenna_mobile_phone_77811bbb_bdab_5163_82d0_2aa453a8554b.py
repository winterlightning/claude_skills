"""Antenna handset with two panel seams; left antenna is intentionally asymmetric.
Construction: Lucide smartphone tangent quarter-circle corners and sparse controls.
Keyshape extremes are read from the live SOLO48 contract, not the stale skill table.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77811bbb-bdab-5163-82d0-2aa453a8554b'
SOURCE_PATH = 'pictographic-primitives/phones/mobile phone blackberry_77811bbb-bdab-5163-82d0-2aa453a8554b.svg'
AUTHOR = 'gpt-6'

class AntennaMobilePhone(Solo48):
    icon_id = 'antenna-mobile-phone'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('phone', 'mobile', 'antenna', 'handset', 'screen', 'device')

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
        box(8,12,40,44,ys=(22,32))
        for y in (22,32): seam(f'panel-{y}',(8,y),(40,y))
        line('antenna',(8,4),(8,16))
        self.relate('connect','antenna','body')
