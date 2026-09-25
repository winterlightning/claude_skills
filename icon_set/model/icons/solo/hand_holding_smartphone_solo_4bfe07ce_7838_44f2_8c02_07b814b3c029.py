"""Plain upright smartphone held from the left; hidden wall removed behind thumb, fingers reduced to one smooth back-of-hand contour."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bfe07ce-7838-44f2-8c02-07b814b3c029'
SOURCE_PATH = 'pictographic-primitives/phones/phone hand hold_4bfe07ce-7838-44f2-8c02-07b814b3c029.svg'
AUTHOR = 'gpt-6'

class HandHoldingSmartphoneSolo(Solo48):
    icon_id = 'hand-holding-smartphone-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('hand', 'holding', 'smartphone', 'phone', 'grip', 'mobile')

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
        # One phone/thumb outline avoids drawing hidden wall through the grip.
        line('top',(22,4),(36,4));arc('tr',(36,4),(40,8),4)
        line('right',(40,8),(40,40));arc('br',(40,40),(36,44),4)
        line('bottom',(36,44),(22,44));arc('bl',(22,44),(18,40),4)
        line('left-low',(18,40),(18,28));line('thumb-bottom',(18,28),(24,28))
        arc('thumb-tip',(24,28),(24,20),4,False)
        line('thumb-top',(24,20),(8,20));arc('knuckles',(8,20),(18,10),10)
        line('left-upper',(18,10),(18,8));arc('tl',(18,8),(22,4),4)
        self.add_contour('outline','top','tr','right','br','bottom','bl','left-low','thumb-bottom','thumb-tip','thumb-top','knuckles','left-upper','tl',closed=True)
        line('palm',(8,20),(8,36));arc('heel',(8,36),(12,40),4,False);line('wrist',(12,40),(12,44))
        self.add_contour('hand','palm','heel','wrist');self.relate('connect','hand','outline')
        arc('thumb-fold',(18,28),(14,32),4)
        self.relate('connect','thumb-fold','outline')
