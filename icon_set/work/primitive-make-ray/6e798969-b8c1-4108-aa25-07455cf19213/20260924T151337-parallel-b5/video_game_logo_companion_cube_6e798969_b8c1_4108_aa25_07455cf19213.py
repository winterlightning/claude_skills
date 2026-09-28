from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='6e798969-b8c1-4108-aa25-07455cf19213'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/video game logo companion cube_6e798969-b8c1-4108-aa25-07455cf19213.svg'
AUTHOR="gpt-6"
PLAN='Corner squares reduced to brackets, connectors to strokes, and medallion ring omitted; central heart and four-corner arrangement retained.'
class Drawing(Solo48):
    icon_id='video-game-logo-companion-cube'
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
        # Four equal corner brackets and four centered connector strokes.
        for j,(x,y,sx,sy) in enumerate(((6,6,1,1),(42,6,-1,1),(6,42,1,-1),(42,42,-1,-1))):
            self.add_polyline(f'corner-{j}',(x+8*sx,y),(x,y),(x,y+8*sy))
        for j,(a,b) in enumerate([((22,6),(26,6)),((22,42),(26,42)),((6,22),(6,26)),((42,22),(42,26))]):
            self.add_line(f'connector-{j}',a,b)
        self.path('heart',(24,20),[('A',(16,20),4,4,False),('L',(24,32)),('L',(32,20)),('A',(24,20),4,4,False)],True)
