"""Vertical receiver with left spine and two projecting ends; paired radii and deep central recess."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfeb8507-5e5b-46a9-af59-f98caa686202'
SOURCE_PATH = 'pictographic-primitives/phones/phone vertical_cfeb8507-5e5b-46a9-af59-f98caa686202.svg'
AUTHOR = 'gpt-6'

class VerticalTelephoneReceiver(Solo48):
    icon_id = 'vertical-telephone-receiver'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('telephone', 'receiver', 'handset', 'vertical', 'call', 'communication')

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
        line('top',(8,34),(8,14));arc('outer-right',(8,14),(18,4),10)
        line('right',(18,4),(36,4));arc('cuff-br',(36,4),(40,8),4)
        line('cuff-bottom-r',(40,8),(40,12));arc('cuff-inner-r',(40,12),(36,16),4)
        line('neck-r',(36,16),(28,16));arc('recess-r',(28,16),(24,20),4,False)
        line('recess',(24,20),(24,28));arc('recess-l',(24,28),(28,32),4,False)
        line('neck-l',(28,32),(36,32));arc('cuff-inner-l',(36,32),(40,36),4)
        line('cuff-bottom-l',(40,36),(40,40));arc('cuff-bl',(40,40),(36,44),4)
        line('left',(36,44),(18,44));arc('outer-left',(18,44),(8,34),10)
        self.add_contour('receiver','top','outer-right','right','cuff-br','cuff-bottom-r','cuff-inner-r','neck-r','recess-r','recess','recess-l','neck-l','cuff-inner-l','cuff-bottom-l','cuff-bl','left','outer-left',closed=True)
