"""Front-camera phone with three flash rays and home bar; screen shortened to allow clear flash spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7cdb5c5-1e28-454e-bf99-436ae1ff9d69'
SOURCE_PATH = 'pictographic-primitives/phones/phone selfie shoot_e7cdb5c5-1e28-454e-bf99-436ae1ff9d69.svg'
AUTHOR = 'gpt-6'

class SmartphoneFrontCameraFlashSolo(Solo48):
    icon_id = 'smartphone-front-camera-flash-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('smartphone', 'camera', 'selfie', 'flash', 'phone', 'screen')

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
        line('top-left',(21,18),(12,18));arc('tl',(12,18),(8,22),4,False)
        line('left',(8,22),(8,40));arc('bl',(8,40),(12,44),4,False)
        line('bottom',(12,44),(36,44));arc('br',(36,44),(40,40),4,False)
        line('right',(40,40),(40,22));arc('tr',(40,22),(36,18),4,False)
        line('top-right',(36,18),(27,18))
        self.add_contour('body','top-left','tl','left','bl','bottom','br','right','tr','top-right')
        arc('camera-top',(21,18),(27,18),3);arc('camera-bottom',(27,18),(21,18),3)
        self.add_contour('camera','camera-top','camera-bottom',closed=True);self.relate('connect','camera','body')
        line('ray-center',(24,4),(24,6));line('ray-left',(8,4),(12,8));line('ray-right',(40,4),(36,8))
        line('home-bar',(21,35),(27,35))
