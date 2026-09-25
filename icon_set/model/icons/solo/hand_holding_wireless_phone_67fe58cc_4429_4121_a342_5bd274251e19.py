"""Right hand gripping a phone with lower bezel and wireless arcs; four signal arcs reduced to one per side, with hidden phone edges omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67fe58cc-4429-4121-a342-5bd274251e19'
SOURCE_PATH = 'pictographic-primitives/phones/wifi transfer hand_67fe58cc-4429-4121-a342-5bd274251e19.svg'
AUTHOR = 'gpt-6'

class HandHoldingWirelessPhone(Solo48):
    icon_id = 'hand-holding-wireless-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('hand', 'phone', 'wireless', 'signal', 'holding', 'mobile')

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
        # One phone/hand contour avoids drawing hidden edges through the thumb.
        line('thumb-top',(34,34),(28,28));arc('thumb-tip',(28,28),(22,34),6,False)
        segments('thumb-low',(22,34),(24,36),(28,40))
        arc('wrist-inner',(28,40),(30,42),2,False)
        line('phone-bottom',(30,42),(16,42));arc('phone-bl',(16,42),(12,38),4)
        segments('phone-left',(12,38),(12,34),(12,22))
        arc('phone-tl',(12,22),(16,18),4);line('phone-top',(16,18),(28,18))
        arc('phone-tr',(28,18),(32,22),4)
        arc('hand-back',(32,22),(42,32),10)
        segments('wrist-outer',(42,32),(42,36),(42,42))
        self.add_contour('outline','thumb-top','thumb-tip',*[f'thumb-low-{i}' for i in range(1,3)],'wrist-inner','phone-bottom','phone-bl',*[f'phone-left-{i}' for i in range(1,3)],'phone-tl','phone-top','phone-tr','hand-back',*[f'wrist-outer-{i}' for i in range(1,3)])
        line('bezel',(12,34),(22,34));self.relate('connect','bezel','outline')
        # One arc per side preserves wireless emission without crowding four arcs.
        arc('signal-left',(6,14),(14,6),8)
        arc('signal-right',(34,6),(42,14),8)
