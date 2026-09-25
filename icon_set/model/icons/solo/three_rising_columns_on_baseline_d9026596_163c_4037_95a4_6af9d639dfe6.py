"""Three narrow rectangular columns stand apart along a horizontal baseline. Their heights increase steadily from left to right, while the open area above them remains blank.
Symbol plan: Three equal-width hollow columns repeat at 16-unit pitch and increase in height. Baseline bridges meet explicit bottom corners without overpainting the column bottoms.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: chart-column-increasing. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9026596-163c-4037-95a4-6af9d639dfe6'
SOURCE_PATH = 'pictographic-primitives/business/line break chart_d9026596-163c-4037-95a4-6af9d639dfe6.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'three-rising-columns-on-baseline'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('three', 'rising', 'columns', 'on', 'baseline')

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

        for j,(x,t) in enumerate([(4,32),(20,20),(36,8)]):rect(f'column-{j}',x,t,x+8,40)
        for j,x in enumerate((12,28)):
         self.add_line(f'baseline-{j}',(x,40),(x+8,40))
         self.relate('connect',f'baseline-{j}',f'column-{j}');self.relate('connect',f'baseline-{j}',f'column-{j+1}')
