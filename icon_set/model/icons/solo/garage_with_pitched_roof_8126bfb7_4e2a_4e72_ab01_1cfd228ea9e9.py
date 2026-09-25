"""A broad garage has a shallow triangular roof projecting beyond two vertical walls. A large rectangular door occupies the centre, with two short horizontal seams inside and a ground line below.
Symbol plan: Symmetric garage shell, triangular roof and a wide roll-up door. One horizontal door seam replaces two; shared door jamb nodes and an 8-unit floor/roof pitch keep all openings clear.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8126bfb7-4e2a-4e72-ab01-1cfd228ea9e9'
SOURCE_PATH = 'pictographic-primitives/building/house garage_8126bfb7-4e2a-4e72-ab01-1cfd228ea9e9.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'garage-with-pitched-roof'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('garage', 'with', 'pitched', 'roof')

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

        self.add_polyline('house',(6,42),(6,18),(24,6),(42,18),(42,42),(34,42),(14,42),closed=True)
        self.add_line('eave',(6,18),(42,18));self.relate('connect','house','eave')
        self.add_polyline('door',(14,42),(14,34),(14,26),(34,26),(34,34),(34,42));self.relate('connect','door','house')
        self.add_line('seam',(14,34),(34,34));self.relate('connect','seam','door')
