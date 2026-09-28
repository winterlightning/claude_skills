"""Capsule camera module with paired lenses; smaller equal lenses preserve clearance inside rounded housing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a9a0bfb-6240-535a-9ba2-c050f5e35304'
SOURCE_PATH = 'pictographic-primitives/phones/phone double camera_7a9a0bfb-6240-535a-9ba2-c050f5e35304.svg'
AUTHOR = 'gpt-6'

class DualCameraModule(Solo48):
    icon_id = 'dual-camera-module'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('camera', 'module', 'dual', 'lenses', 'phone', 'hardware')

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
        line('top',(20,8),(28,8))
        arc('right',(28,8),(28,40),16)
        line('bottom',(28,40),(20,40))
        arc('left',(20,40),(20,8),16)
        self.add_contour('housing','top','right','bottom','left',closed=True)
        for x in (16,32):circle(f'lens-{x}',x,24,3)
