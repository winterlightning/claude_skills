"""Child tricycle with high-backed seat, curved frame, paired wheels and front basket. Equal wheel radius7; bounds6,6 to42,42.
Construction reference: Lucide bike: equal circular wheels and simple frame.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ff4ebdd-5754-482c-9fb2-040f1c9eaa90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'child-cycle-with-front-basket-batch-018-02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('tricycle',)
    def build(self):
        for n,x in [('rear',13),('front',35)]:self.circle(n,x,35,7)
        self.path('frame',(13,28),[('L',(15,22)),('L',(26,22)),('C',(33,18),(30,22),(32,20)),('L',(35,28))])
        self.path('seat',(15,22),[('L',(11,9)),('A',(17,9),3,3,True),('L',(20,14)),('L',(25,14))])
        self.add_polyline('stem',(27,6),(31,6),(32,12),(33,18))
        self.add_polyline('basket',(32,12),(42,12),(40,20),(34,20))
        for a,b in [('frame','rear'),('frame','front'),('frame','seat'),('frame','stem'),('stem','basket')]:self.relate('connect',a,b)

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
        self.path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
