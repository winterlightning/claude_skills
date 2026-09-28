"""Two long parallel side rails lean toward the right. Three horizontal rungs connect them at regular intervals, with the rails extending beyond the uppermost and lowest rungs.
Symbol plan: Two matching rails lean right with a shared 1:3 slope. Three horizontal rungs repeat at a 12-unit vertical pitch and attach at explicit rail nodes. No details omitted.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: ruler. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f849ffb1-ea4f-54f7-9d2c-17aceb891e70'
SOURCE_PATH = 'pictographic-primitives/business/ladder_f849ffb1-ea4f-54f7-9d2c-17aceb891e70.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'leaning-ladder-with-three-rungs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('leaning', 'ladder', 'with', 'three', 'rungs')

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

        for n,x in [('left',6),('right',30)]:
         self.add_polyline(n+'-rail',(x,42),(x+2,36),(x+6,24),(x+10,12),(x+12,6))
        for j,(x,y) in enumerate([(8,36),(12,24),(16,12)]):
         self.add_line(f'rung-{j}',(x,y),(x+24,y))
         for n in ('left','right'):self.relate('connect',f'rung-{j}',n+'-rail')
