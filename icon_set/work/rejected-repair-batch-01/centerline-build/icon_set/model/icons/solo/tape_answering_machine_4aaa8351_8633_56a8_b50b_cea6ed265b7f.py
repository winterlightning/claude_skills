"""Low answering machine with paired circular reels, connecting tape with the secondary control omitted for clear spacing.
Construction: Lucide smartphone rounded corners; voicemail reel tangents.
Keyshape extremes are read from the live SOLO48 contract, not the stale skill table.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aaa8351-8633-56a8-b50b-cea6ed265b7f'
SOURCE_PATH = 'pictographic-primitives/phones/answer machine_4aaa8351-8633-56a8-b50b-cea6ed265b7f.svg'
AUTHOR = 'gpt-6'

class TapeAnsweringMachine(Solo48):
    icon_id = 'tape-answering-machine'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('answering', 'machine', 'tape', 'recorder', 'telephone', 'message')

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
        box(4,8,44,40)
        # Matching tape reels joined along their bottom tangents.
        for x in (16,32): circle(f'reel-{x}',x,21,3)
        line('tape',(16,24),(32,24))
        for x in (16,32): self.relate('connect','tape',f'reel-{x}')
