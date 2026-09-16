"""Ringing horizontal receiver with three equally weighted sound rays; receiver shortened to leave room above."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6249c2b9-f5e4-4b2b-81c7-a4a513a95c3c'
SOURCE_PATH = 'pictographic-primitives/phones/phone incoming call_6249c2b9-f5e4-4b2b-81c7-a4a513a95c3c.svg'
AUTHOR = 'gpt-6'

class RingingTelephoneReceiver(Solo48):
    icon_id = 'ringing-telephone-receiver'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('telephone', 'receiver', 'ringing', 'call', 'sound', 'handset')

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
        line('top',(14,22),(34,22));arc('outer-r',(34,22),(44,32),10)
        line('right',(44,32),(44,36));arc('br',(44,36),(40,40),4)
        line('bottom-r',(40,40),(36,40));arc('inner-r',(36,40),(32,36),4)
        line('rise-r',(32,36),(32,35));arc('recess-r',(32,35),(28,31),4,False)
        line('recess',(28,31),(20,31));arc('recess-l',(20,31),(16,35),4,False)
        line('rise-l',(16,35),(16,36));arc('inner-l',(16,36),(12,40),4)
        line('bottom-l',(12,40),(8,40));arc('bl',(8,40),(4,36),4)
        line('left',(4,36),(4,32));arc('outer-l',(4,32),(14,22),10)
        self.add_contour('receiver','top','outer-r','right','br','bottom-r','inner-r','rise-r','recess-r','recess','recess-l','rise-l','inner-l','bottom-l','bl','left','outer-l',closed=True)
        line('ray-center',(24,8),(24,13))
        line('ray-left',(8,8),(12,12));line('ray-right',(40,8),(36,12))
