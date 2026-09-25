"""Table tennis paddle, broad diagonal grip and detached ball. Round upper-right face, diagonal face seam; bounds 6,6 to42,42.
Construction reference: No useful exact Lucide match; circle and tangent handle construction.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f81bb0f5-e79c-5478-8158-f8e1d2294934'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'table-tennis-paddle-and-ball-solo-b016'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'kids'
    aliases = ()
    keywords = ('toys', 'ping', 'pong')
    def build(self):
        self.path('outline',(13,18),[('A',(25,6),12,12,True),('A',(37,18),12,12,True),('A',(25,30),12,12,True),('L',(21,30)),('L',(12,42)),('L',(6,36)),('L',(15,27)),('C',(13,18),(14,24),(13,21))],True)
        self.add_line('seam',(13,18),(25,30));self.relate('connect','seam','outline')
        self.circle('ball',39,39,3)

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
