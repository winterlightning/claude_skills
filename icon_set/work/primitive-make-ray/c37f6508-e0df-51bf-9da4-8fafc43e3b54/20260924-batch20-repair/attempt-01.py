from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c37f6508-e0df-51bf-9da4-8fafc43e3b54'
SOURCE_PATH='pictographic-primitives/war/death rip_c37f6508-e0df-51bf-9da4-8fafc43e3b54.svg'
AUTHOR='gpt-6'
PLAN='Arched RIP gravestone and plinth. Widen stone to SQUARE6,6–42,42 and raise inscription for baseline clearance. Preserve all letters. No useful exact Lucide tombstone match.'
class Drawing(Solo48):
    icon_id='death-rip'
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
        self.add_line('stone-left',(6,34),(6,18))
        self.add_arc('stone-arch',(6,18),(42,18),radius_x=18,radius_y=12)
        self.add_line('stone-right',(42,18),(42,34))
        self.add_contour('stone','stone-left','stone-arch','stone-right')
        self.add_polyline('plinth',(6,34),(42,34),(42,42),(6,42),closed=True);self.relate('connect','stone','plinth')
        for label,x in [('r',14),('p',32)]:
         self.add_polyline(label+'-stem',(x,26),(x,22),(x,16))
         self.add_arc(label+'-bowl',(x,16),(x,22),radius_x=4,radius_y=3)
         self.relate('connect',label+'-stem',label+'-bowl')
        self.add_line('r-leg',(14,22),(18,26));self.relate('connect','r-leg','r-stem');self.relate('connect','r-leg','r-bowl')
        self.add_line('i',(24,16),(24,26))
