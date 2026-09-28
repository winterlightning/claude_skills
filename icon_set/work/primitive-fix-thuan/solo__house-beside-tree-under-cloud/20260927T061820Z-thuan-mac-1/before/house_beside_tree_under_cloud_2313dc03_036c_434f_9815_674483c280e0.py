"""A small gabled house with an arched door stands beside a tall pointed tree. A rounded cloud floats above the house, and a single ground line joins the building and tree.
Symbol plan: Natural house-and-tree scene under a small capsule cloud. One simple gable and one pointed tree with a rounded base retain the source arrangement. Omit the undersized door and extra cloud lobe.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house, cloud, trees. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2313dc03-036c-434f-9815-674483c280e0'
SOURCE_PATH = 'pictographic-primitives/building/house nature_2313dc03-036c-434f-9815-674483c280e0.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'house-beside-tree-under-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'beside', 'tree', 'under', 'cloud')

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

        rect('cloud',6,6,24,14,4)
        self.add_polyline('house',(6,42),(6,31),(15,23),(24,31),(24,42))
        segments('ground',(6,42),(24,42),(37,42),(42,42));self.add_contour('baseline','ground-1','ground-2','ground-3');self.relate('connect','house','baseline')
        self.add_line('tree-right',(37,18),(42,28));self.add_arc('tree-bottom-right',(42,28),(37,33),radius_x=5)
        self.add_arc('tree-bottom-left',(37,33),(32,28),radius_x=5);self.add_line('tree-left',(32,28),(37,18))
        self.add_contour('tree','tree-right','tree-bottom-right','tree-bottom-left','tree-left',closed=True)
        self.add_line('trunk',(37,33),(37,42));self.relate('connect','trunk','tree');self.relate('connect','trunk','baseline')
