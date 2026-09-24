from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='59b04c40-2006-4e31-a230-a6be869385d4'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shopping pay hide advertising_59b04c40-2006-4e31-a230-a6be869385d4.svg'
AUTHOR='gpt-6'
PLAN='Dollar coin suppression. Open circular boundary around slash; real stem joins at ring extrema and dollar knots. SQUARE6,6–42,42. Preserve full dollar and slash; manual-review candidate if gate fails.'
class Drawing(Solo48):
    icon_id='shopping-pay-hide-advertising'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        for n,a,b in [('nw',(6,24),(24,6)),('se',(42,24),(24,42))]:self.add_arc(n,a,b,radius_x=18)
        self.add_bezier('dollar-upper',(31,16),((28,15),(26,15),(24,15)),((15,15),(15,24),(24,24)))
        self.add_bezier('dollar-lower',(24,24),((33,24),(33,33),(24,33)),((22,33),(20,33),(17,32)))
        self.add_contour('dollar','dollar-upper','dollar-lower')
        self.add_line('stem-top',(24,6),(24,15));self.relate('connect','stem-top','dollar');self.relate('connect','stem-top','nw')
        self.add_line('stem-bottom',(24,33),(24,42));self.relate('connect','stem-bottom','dollar');self.relate('connect','stem-bottom','se')
        self.add_polyline('slash',(6,42),(24,24),(42,6));self.relate('connect','slash','dollar')
