"""Notched smartphone with circular home button; outer contour carries the notch without a redundant inner screen frame.
Construction: Lucide smartphone tangent quarter-circle corners and sparse controls.
Keyshape extremes are read from the live SOLO48 contract, not the stale skill table.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '318398ff-29a6-5b27-9546-cef465417560'
SOURCE_PATH = 'pictographic-primitives/phones/iphone x_318398ff-29a6-5b27-9546-cef465417560.svg'
AUTHOR = 'gpt-6'

class NotchedSmartphoneWithHomeButton(Solo48):
    icon_id = 'notched-smartphone-with-home-button'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('smartphone', 'phone', 'notch', 'screen', 'button', 'mobile')

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
        # One coherent notched silhouette; mirrored about x=24.
        line('top-left',(12,4),(16,4))
        arc('notch-left',(16,4),(20,8),4,False)
        line('notch-floor',(20,8),(28,8))
        arc('notch-right',(28,8),(32,4),4,False)
        line('top-right',(32,4),(36,4))
        arc('corner-tr',(36,4),(40,8),4)
        line('right',(40,8),(40,40))
        arc('corner-br',(40,40),(36,44),4)
        line('bottom',(36,44),(12,44))
        arc('corner-bl',(12,44),(8,40),4)
        line('left',(8,40),(8,8))
        arc('corner-tl',(8,8),(12,4),4)
        self.add_contour('body','top-left','notch-left','notch-floor','notch-right','top-right','corner-tr','right','corner-br','bottom','corner-bl','left','corner-tl',closed=True)
        circle('home-button',24,33,2)
