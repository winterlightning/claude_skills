from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='9906051d-60e6-48a1-85dc-e14a0d83a72d'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/turn 1_9906051d-60e6-48a1-85dc-e14a0d83a72d.svg'
AUTHOR="gpt-6"
PLAN='Outlined narrow route reduced to a vertical stroke with opposing branch ticks inside the diamond.'
class Drawing(Solo48):
    icon_id='turn-1'
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
        self.add_polyline('diamond',(24,6),(42,24),(24,42),(6,24),closed=True)
        self.add_polyline('route',(24,18),(24,24),(24,30))
        self.add_polyline('upper-branch',(24,20),(26,20))
        self.add_polyline('lower-branch',(24,28),(22,28))
        self.relate('connect','route','upper-branch')
        self.relate('connect','route','lower-branch')
