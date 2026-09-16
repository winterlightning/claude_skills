"""Smartphone rear with a vertical capsule camera housing; inner lens mark omitted because three nested detail levels cannot maintain clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37566550-27a5-4058-bc91-e93e0b26c2fc'
SOURCE_PATH = 'pictographic-primitives/phones/samsung_37566550-27a5-4058-bc91-e93e0b26c2fc.svg'
AUTHOR = 'gpt-6'

class SmartphoneRearCamera(Solo48):
    icon_id = 'smartphone-rear-camera'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartphone', 'camera', 'back', 'rear', 'lens', 'phone')

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
        box(8,4,40,44)
        # The small camera housing is one vertical capsule near the left edge.
        arc('camera-top',(17,17),(25,17),4)
        line('camera-right',(25,17),(25,23))
        arc('camera-bottom',(25,23),(17,23),4)
        line('camera-left',(17,23),(17,17))
        self.add_contour('camera','camera-top','camera-right','camera-bottom','camera-left',closed=True)
