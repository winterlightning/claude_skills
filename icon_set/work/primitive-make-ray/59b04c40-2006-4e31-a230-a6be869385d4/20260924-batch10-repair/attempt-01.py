from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='59b04c40-2006-4e31-a230-a6be869385d4'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shopping pay hide advertising_59b04c40-2006-4e31-a230-a6be869385d4.svg'
AUTHOR='gpt-6'
PLAN='Coin with dollar and suppression slash. Dollar upper and lower stem shortened; SQUARE6,6–42,42. No useful exact Lucide match; preserve crossing symbol for validation.'
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
        self.circle('coin',24,24,18)
        self.add_bezier('dollar',(31,16),((17,9),(12,24),(24,24)),((36,24),(31,39),(17,32)))
        self.add_line('stem-top',(24,10),(24,14));self.relate('connect','stem-top','dollar')
        self.add_line('stem-bottom',(24,34),(24,38));self.relate('connect','stem-bottom','dollar')
        self.add_polyline('slash',(6,42),(24,24),(42,6));self.relate('connect','slash','coin');self.relate('connect','slash','dollar')
