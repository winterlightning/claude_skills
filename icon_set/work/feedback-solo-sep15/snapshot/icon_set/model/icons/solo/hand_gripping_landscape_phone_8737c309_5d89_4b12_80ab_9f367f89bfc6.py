"""Landscape phone in an upturned grip; four fingers reduced to three joined rounded knuckles and slight tilt removed for clear geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8737c309-5d89-4b12-80ab-9f367f89bfc6'
SOURCE_PATH = 'pictographic-primitives/phones/phone hand hold_8737c309-5d89-4b12-80ab-9f367f89bfc6.svg'
AUTHOR = 'gpt-6'

class HandGrippingLandscapePhone(Solo48):
    icon_id = 'hand-gripping-landscape-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('hand', 'phone', 'landscape', 'holding', 'grip', 'mobile')

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
        box(6,14,42,30,rad=3,xs=(10,14,18,26,34))
        # Three joined finger arches share their crease nodes and phone contacts.
        line('fingers-left',(10,14),(10,10))
        for x in (10,18,26):arc(f'knuckle-{x}',(x,10),(x+8,10),4)
        line('fingers-right',(34,10),(34,14))
        self.add_contour('fingers','fingers-left','knuckle-10','knuckle-18','knuckle-26','fingers-right')
        self.relate('connect','fingers','body')
        for x in (18,26):
            line(f'crease-{x}',(x,10),(x,14))
            self.relate('connect',f'crease-{x}','fingers');self.relate('connect',f'crease-{x}','body')
        line('palm-left',(14,30),(14,34));arc('palm-heel',(14,34),(18,38),4,False);line('wrist-left',(18,38),(18,42))
        self.add_contour('palm','palm-left','palm-heel','wrist-left');self.relate('connect','palm','body')
        line('thumb',(26,30),(34,22));self.relate('connect','thumb','body')
        line('hand-right',(34,30),(34,34));arc('hand-heel',(34,34),(30,38),4);line('wrist-right',(30,38),(30,42))
        self.add_contour('hand','hand-right','hand-heel','wrist-right');self.relate('connect','hand','body')
