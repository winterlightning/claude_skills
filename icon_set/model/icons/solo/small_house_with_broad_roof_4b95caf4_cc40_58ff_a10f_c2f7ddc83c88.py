"""A compact rectangular house has rounded lower corners and a wide trapezoidal roof with softened edges. One tall arched doorway opens centrally in the otherwise blank front wall.
Symbol plan: Broad trapezoidal roof over a compact rounded house, with a centered arched doorway. Roof corners use the standard round joins; lower wall turns and door arch share radius 4.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b95caf4-cc40-58ff-a10f-c2f7ddc83c88'
SOURCE_PATH = 'pictographic-primitives/building/house home building_4b95caf4-cc40-58ff-a10f-c2f7ddc83c88.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'small-house-with-broad-roof'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('small', 'house', 'with', 'broad', 'roof')

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

        self.add_polyline('roof',(6,18),(12,6),(36,6),(42,18),(40,18),(8,18),closed=True)
        self.add_line('wall-left',(8,18),(8,38));self.add_arc('corner-left',(8,38),(12,42),radius_x=4,sweep=False)
        segments('floor',(12,42),(20,42),(28,42),(36,42))
        self.add_arc('corner-right',(36,42),(40,38),radius_x=4,sweep=False);self.add_line('wall-right',(40,38),(40,18))
        self.add_contour('walls','wall-left','corner-left','floor-1','floor-2','floor-3','corner-right','wall-right');self.relate('connect','walls','roof')
        self.add_line('door-left',(20,42),(20,34));self.add_arc('door-arch',(20,34),(28,34),radius_x=4);self.add_line('door-right',(28,34),(28,42))
        self.add_contour('door','door-left','door-arch','door-right');self.relate('connect','door','walls')
