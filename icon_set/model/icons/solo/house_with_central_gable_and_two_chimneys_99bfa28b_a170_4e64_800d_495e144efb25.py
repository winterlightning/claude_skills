"""A broad house has a central projecting gable above an arched doorway. Two lower roof wings extend to either side, each topped by a narrow chimney with a short cap.
Symbol plan: Mirrored low roof wings, central gable, capped chimneys and arched doorway. Each chimney is one vertical stroke at x12 or x36 with an 8-unit cap; omit separate gable wall seams.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '99bfa28b-a170-4e64-800d-495e144efb25'
SOURCE_PATH = 'pictographic-primitives/building/house retro_99bfa28b-a170-4e64-800d-495e144efb25.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'house-with-central-gable-and-two-chimneys'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('house', 'with', 'central', 'gable', 'and', 'two', 'chimneys')

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

        self.add_polyline('house',(6,42),(6,26),(12,18),(16,18),(24,10),(32,18),(36,18),(42,26),(42,42),(28,42),(20,42),closed=True)
        for n,x in [('left',12),('right',36)]:
         self.add_line(n+'-chimney',(x,6),(x,18));self.add_polyline(n+'-cap',(x-4,6),(x,6),(x+4,6))
         self.relate('connect',n+'-chimney',n+'-cap');self.relate('connect',n+'-chimney','house')
        self.add_line('door-left',(20,42),(20,34));self.add_arc('door-arch',(20,34),(28,34),radius_x=4);self.add_line('door-right',(28,34),(28,42))
        self.add_contour('door','door-left','door-arch','door-right');self.relate('connect','door','house')
