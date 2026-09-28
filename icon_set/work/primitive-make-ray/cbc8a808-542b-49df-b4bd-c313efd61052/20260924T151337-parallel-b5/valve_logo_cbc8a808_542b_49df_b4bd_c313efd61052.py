from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='cbc8a808-542b-49df-b4bd-c313efd61052'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg'
AUTHOR="gpt-6"
PLAN='Five-letter VALVE wordmark retained. Widening letter openings consumes spacing between letters; no readable compliant one-line solution achieved.'
class Drawing(Solo48):
    icon_id='valve-logo'
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
    def path(self,n,p,ops,closed=False):
        members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';end=op[1]
            if op[0]=='L': self.add_line(eid,p,end)
            elif op[0]=='A': self.add_arc(eid,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            else: self.add_bezier(eid,p,(op[2],op[3],end))
            p=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        self.add_polyline('v-first',(4,8),(8,40),(12,8))
        self.add_polyline('a-sides',(14,40),(18,8),(22,40))
        self.add_line('a-bar',(16,24),(20,24))
        self.add_polyline('l',(25,8),(25,40),(29,40))
        self.add_polyline('v-second',(31,8),(34,40),(37,8))
        self.add_polyline('e',(44,8),(40,8),(40,24),(40,40),(44,40))
        self.add_line('e-middle',(40,24),(44,24))
        self.relate('connect','e','e-middle')
