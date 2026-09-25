"""A simple peaked-roof house has a rounded arched doorway and a chimney on its right roof slope. A short wavering smoke line rises above the chimney opening.
Symbol plan: Compact peaked house with an open arched doorway and a right chimney. A broad smoke curl provides the right/top extent. Reduce chimney to one stroke and omit roof overhangs.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab402af4-7fa5-59c6-8861-78bb8c0e3f7e'
SOURCE_PATH = 'pictographic-primitives/building/house chimney smoke_ab402af4-7fa5-59c6-8861-78bb8c0e3f7e.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'house-with-smoking-chimney'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'with', 'smoking', 'chimney')

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

        self.add_polyline('house',(6,42),(6,30),(20,18),(34,30),(34,42),(24,42),(16,42),closed=True)
        self.add_line('chimney',(34,30),(34,18));self.relate('connect','chimney','house')
        self.add_arc('smoke',(34,10),(42,6),radius_x=8,radius_y=4,sweep=False)
        self.add_line('door-left',(16,42),(16,36));self.add_arc('door-arch',(16,36),(24,36),radius_x=4);self.add_line('door-right',(24,36),(24,42))
        self.add_contour('door','door-left','door-arch','door-right');self.relate('connect','door','house')
