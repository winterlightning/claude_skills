"""Downturned telephone receiver above nine keys; tiny key rectangles reduced to dots."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ef4d103-1790-43af-a394-fdf01fa24a3f'
SOURCE_PATH = 'pictographic-primitives/phones/phone dial_7ef4d103-1790-43af-a394-fdf01fa24a3f.svg'
AUTHOR = 'gpt-6'

class TelephoneDialPad(Solo48):
    icon_id = 'telephone-dial-pad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('telephone', 'dial', 'keypad', 'receiver', 'call', 'keys')

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
        # Symmetric downturned receiver above a 3-by-3 keypad.
        line('top',(16,6),(32,6));arc('right-shoulder',(32,6),(42,16),10)
        segments('receiver-bottom',(42,16),(42,17),(34,17),(34,14),(14,14),(14,17),(6,17),(6,16))
        arc('left-shoulder',(6,16),(16,6),10)
        self.add_contour('receiver','top','right-shoulder',*[f'receiver-bottom-{i}' for i in range(1,8)],'left-shoulder',closed=True)
        for row in range(3):
            for col in range(3): self.add_dot(f'key-{row}-{col}',(12+12*col,26+8*row))
