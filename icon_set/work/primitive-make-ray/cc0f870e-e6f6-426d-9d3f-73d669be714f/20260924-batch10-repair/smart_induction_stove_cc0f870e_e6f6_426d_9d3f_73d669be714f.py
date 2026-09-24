from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cc0f870e-e6f6-426d-9d3f-73d669be714f'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smart induction stove_cc0f870e-e6f6-426d-9d3f-73d669be714f.svg'
AUTHOR='gpt-6'
PLAN='Smart hob retains perspective top, wireless mark and front controls. VRECT_L8,4–40,44 adds depth; secondary base lip omitted and three panels reduced to two. Lucide wifi concentric construction simplified to one arch and dot.'
class Drawing(Solo48):
    icon_id='smart-induction-stove'
    keyshape=Keyshape.VRECT_L
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
        self.add_polyline('top',(8,32),(12,4),(36,4),(40,32))
        self.add_polyline('front',(8,32),(24,32),(40,32),(40,44),(24,44),(8,44),closed=True);self.relate('connect','top','front')
        self.add_line('division',(24,32),(24,44));self.relate('connect','division','front')
        self.add_arc('wifi',(19,16),(29,16),radius_x=5,radius_y=3)
        self.add_dot('signal',(24,24))
