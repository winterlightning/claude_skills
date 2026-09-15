"""Desk rotary telephone with domed sides and flat foot; cradle posts absorbed into genuine receiver/base contacts."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6045a6f-cf65-4a9e-88d7-2c4f251336f9'
SOURCE_PATH = 'pictographic-primitives/phones/phone retro_c6045a6f-cf65-4a9e-88d7-2c4f251336f9.svg'
AUTHOR = 'gpt-6'

class DeskRotaryTelephone(Solo48):
    icon_id = 'desk-rotary-telephone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('telephone', 'rotary', 'desk', 'vintage', 'dial', 'landline')

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
        ellipse('base-left',(14,17),(6,36),8,19,False)
        line('foot-left',(6,36),(6,42));line('foot',(6,42),(42,42));line('foot-right',(42,42),(42,36))
        ellipse('base-right',(42,36),(34,17),8,19,False)
        self.add_contour('base','base-left','foot-left','foot','foot-right','base-right')
        self.relate('connect','base','receiver')
        circle('dial',24,29,4)
