"""A single angular chart line rises and falls through several vertical runs joined by horizontal shoulders. The highest plateau sits near the right, followed by a short downward segment.
Symbol plan: One continuous Kagi line uses an 8-unit horizontal pitch and alternating levels, with its highest shoulder on the right. Preserve the asymmetric data sequence and use standard round joins.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: chart-column-increasing. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '58cabe99-3ea5-58a4-9b43-e6b3b23afda6'
SOURCE_PATH = 'pictographic-primitives/business/kagi chart_58cabe99-3ea5-58a4-9b43-e6b3b23afda6.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'kagi-chart-with-alternating-steps'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('kagi', 'chart', 'with', 'alternating', 'steps')

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

        self.add_polyline('chart',(4,28),(4,20),(12,20),(12,40),(20,40),(20,24),(28,24),(28,32),(36,32),(36,8),(44,8),(44,20))
