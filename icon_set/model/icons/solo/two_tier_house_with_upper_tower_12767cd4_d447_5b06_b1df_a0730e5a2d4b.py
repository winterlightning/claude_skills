"""A wide lower house supports a narrower upper storey capped by a triangular roof. A second broad roof crosses the lower level, above a small rectangular doorway on the right.
Symbol plan: Two centered roof tiers with an upper tower, mirrored on x24. Shared eave nodes define each level. Omit the tiny lower door because two roof levels need the full height budget.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '12767cd4-d447-5b06-b1df-a0730e5a2d4b'
SOURCE_PATH = 'pictographic-primitives/building/house modern_12767cd4-d447-5b06-b1df-a0730e5a2d4b.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'two-tier-house-with-upper-tower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('two', 'tier', 'house', 'with', 'upper', 'tower')

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

        self.add_polyline('upper-roof',(16,14),(24,6),(32,14),closed=True)
        self.add_line('tower-left',(16,14),(16,22));self.add_line('tower-right',(32,14),(32,22))
        self.add_polyline('lower-roof',(6,30),(12,22),(16,22),(32,22),(36,22),(42,30),(40,30),(8,30),closed=True)
        for n in ('tower-left','tower-right'):
         self.relate('connect',n,'upper-roof');self.relate('connect',n,'lower-roof')
        self.add_polyline('walls',(8,30),(8,42),(40,42),(40,30));self.relate('connect','walls','lower-roof')
