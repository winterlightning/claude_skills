"""A circular mirror sits inside a thick ring-shaped frame connected to a diagonal lower-left handle. The handle has a rounded end, and the reflecting face is blank.
Symbol plan: Circular mirror at (30,16), radius 10, with a diagonal handle attached at the exact 3:4 radial point (24,24). Omit the duplicate inner frame ring; the blank mirror remains large and clear.
Keyshape: CIRCLE; centerline extremes radius 20 about (24,24).
Construction reference: brush; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '53fc57d4-b81d-436c-a889-4e9853c9ecec'
SOURCE_PATH = 'pictographic-primitives/beauty/hand mirror_53fc57d4-b81d-436c-a889-4e9853c9ecec.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'round-hand-mirror-with-handle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('round', 'hand', 'mirror', 'with', 'handle')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_arc('mirror-a',(24,24),(36,8),radius_x=10)
        self.add_arc('mirror-b',(36,8),(24,24),radius_x=10)
        self.add_contour('mirror','mirror-a','mirror-b',closed=True)
        self.add_line('handle',(24,24),(12,40))
        self.relate('connect','handle','mirror')
