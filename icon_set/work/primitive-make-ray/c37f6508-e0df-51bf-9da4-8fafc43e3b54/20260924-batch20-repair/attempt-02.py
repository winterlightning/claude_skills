from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c37f6508-e0df-51bf-9da4-8fafc43e3b54'
SOURCE_PATH='pictographic-primitives/war/death rip_c37f6508-e0df-51bf-9da4-8fafc43e3b54.svg'
AUTHOR='gpt-6'
PLAN='Wider HRECT_L4,8–44,40 tombstone. Plinth reduced to baseline to make room for RIP. Preserve horizontal inscription; no useful exact Lucide reference.'
class Drawing(Solo48):
    icon_id='death-rip'
    keyshape=Keyshape.HRECT_L
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
        self.add_line('stone-left',(4,40),(4,20))
        self.add_arc('stone-arch',(4,20),(44,20),radius_x=20,radius_y=12)
        self.add_line('stone-right',(44,20),(44,40))
        self.add_contour('stone','stone-left','stone-arch','stone-right')
        self.add_line('base',(4,40),(44,40));self.relate('connect','stone','base')
        for label,x in [('r',12),('p',32)]:
         self.add_polyline(label+'-stem',(x,32),(x,26),(x,20))
         self.add_arc(label+'-bowl',(x,20),(x,26),radius_x=4,radius_y=3)
         self.relate('connect',label+'-stem',label+'-bowl')
        self.add_line('r-leg',(12,26),(16,32));self.relate('connect','r-leg','r-stem');self.relate('connect','r-leg','r-bowl')
        self.add_line('i',(24,20),(24,32))
