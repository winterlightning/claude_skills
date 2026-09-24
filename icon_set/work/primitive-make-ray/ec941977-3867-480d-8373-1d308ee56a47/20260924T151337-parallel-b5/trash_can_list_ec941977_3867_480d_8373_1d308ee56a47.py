from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='ec941977-3867-480d-8373-1d308ee56a47'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/trash can list_ec941977-3867-480d-8373-1d308ee56a47.svg'
AUTHOR="gpt-6"
PLAN='Two list rows replace three; thin lid replaces double outline; broad symmetric bin and handle.'
class Drawing(Solo48):
    icon_id='trash-can-list'
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
        self.add_polyline('lid',(8,12),(16,12),(32,12),(40,12))
        self.path('handle',(16,12),[('L',(16,8)),('A',(20,4),4,4,True),('L',(28,4)),('A',(32,8),4,4,True),('L',(32,12))])
        self.relate('connect','lid','handle')
        self.path('bin',(8,12),[('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,12))])
        self.relate('connect','lid','bin')
        for j,y in enumerate((23,33)):
            self.add_line(f'list-{j}',(18,y),(30,y))
