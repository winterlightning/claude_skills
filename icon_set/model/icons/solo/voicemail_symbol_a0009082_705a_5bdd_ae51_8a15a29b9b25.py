"""Paired voicemail loops connected along their bottom tangents; live keyshape forces taller oval loops than the circular reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0009082-705a-5bdd-ae51-8a15a29b9b25'
SOURCE_PATH = 'pictographic-primitives/phones/voice mail_a0009082-705a-5bdd-ae51-8a15a29b9b25.svg'
AUTHOR = 'gpt-6'

class VoicemailSymbolA0009082(Solo48):
    icon_id = 'voicemail-symbol-a0009082'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('voicemail', 'message', 'audio', 'recording', 'loops', 'telephone')

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
        # Equal loops and a shared bottom tangent, independently rebuilt on SOLO48.
        for x in (11,37):
            self.add_arc(f'loop-{x}-a',(x,40),(x,8),radius_x=7,radius_y=16)
            self.add_arc(f'loop-{x}-b',(x,8),(x,40),radius_x=7,radius_y=16)
            self.add_contour(f'loop-{x}',f'loop-{x}-a',f'loop-{x}-b',closed=True)
        line('bridge',(11,40),(37,40))
        for x in (11,37):self.relate('connect','bridge',f'loop-{x}')
