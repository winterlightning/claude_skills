"""A broad arch connects two earcups with rounded outer edges and flat inner sides. The headband meets the upper outer corners, leaving a large empty opening between the pads.
Symbol plan: Semicircular headband with two mirrored pads having flat inner edges and rounded lower outer corners. Shared x=24 axis and radius-4 outer turns.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: headphones; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'abfe0bd7-6786-4438-bd91-8302678cec4a'
SOURCE_PATH = 'pictographic-primitives/audio/headphones_abfe0bd7-6786-4438-bd91-8302678cec4a.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'headphones-with-flat-inner-pads'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    aliases = ()
    keywords = ('headphones', 'with', 'flat', 'inner', 'pads')

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

        self.add_arc('band',(6,24),(42,24),radius_x=18)
        for n,l,r in [('left',6,16),('right',32,42)]:
         if n=='left':
          self.add_line('l-out',(6,24),(6,38));self.add_arc('l-round',(6,38),(10,42),radius_x=4,sweep=False)
          segments('l-inner',(10,42),(16,42),(16,24),(6,24))
          self.add_contour(n,'l-out','l-round','l-inner-1','l-inner-2','l-inner-3',closed=True)
         else:
          segments('r-inner',(42,24),(32,24),(32,42),(38,42))
          self.add_arc('r-round',(38,42),(42,38),radius_x=4,sweep=False);self.add_line('r-out',(42,38),(42,24))
          self.add_contour(n,'r-inner-1','r-inner-2','r-inner-3','r-round','r-out',closed=True)
         self.relate('connect','band',n)
