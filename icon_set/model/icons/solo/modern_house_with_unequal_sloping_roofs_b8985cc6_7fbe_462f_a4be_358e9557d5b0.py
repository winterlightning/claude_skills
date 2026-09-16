"""Two adjoining house sections have rooflines sloping in opposite directions around a tall central wall. A round upper window sits above a rectangular doorway, beside a smaller arched entrance.
Symbol plan: Two adjoining volumes retain the opposing unequal roof slopes and tall central wall. One rectangular doorway replaces the two small entries; omit the upper circular window and the lower internal divider.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8985cc6-7fbe-462f-a4be-358e9557d5b0'
SOURCE_PATH = 'pictographic-primitives/building/house modern_b8985cc6-7fbe-462f-a4be-358e9557d5b0.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'modern-house-with-unequal-sloping-roofs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('modern', 'house', 'with', 'unequal', 'sloping', 'roofs')

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

        self.add_polyline('house',(6,42),(6,30),(24,22),(24,6),(42,18),(42,42),(34,42),(26,42),closed=True)
        self.add_polyline('door',(26,42),(26,30),(34,30),(34,42));self.relate('connect','door','house')
