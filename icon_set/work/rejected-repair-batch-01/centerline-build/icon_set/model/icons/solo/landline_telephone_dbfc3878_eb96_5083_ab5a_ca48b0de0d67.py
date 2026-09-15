"""Compact receiver above a rounded U-shaped landline base; no dial added to the plain source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbfc3878-eb96-5083-ab5a-ca48b0de0d67'
SOURCE_PATH = 'pictographic-primitives/phones/phone landline_dbfc3878-eb96-5083-ab5a-ca48b0de0d67.svg'
AUTHOR = 'gpt-6'

class LandlineTelephone(Solo48):
    icon_id = 'landline-telephone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('telephone', 'landline', 'receiver', 'base', 'handset', 'desk')

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
        compact_receiver()
        line('base-left',(10,26),(10,36));arc('base-bl',(10,36),(16,42),6,False)
        line('base-bottom',(16,42),(32,42));arc('base-br',(32,42),(38,36),6,False)
        line('base-right',(38,36),(38,26))
        self.add_contour('base','base-left','base-bl','base-bottom','base-br','base-right')
