"""Smooth circular cranium, rounded chin and continuous neck; retain source facing direction and open neck base.
Construction: Human reference user.svg: circular head vocabulary; continuous-neck source profile, no detached gap.
Omissions: Fine lip serrations omitted to avoid crowded strokes.
Keyshape VRECT_L: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0da0f78f-cd68-48d5-8070-b71070bed549'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bipolar disorder symptoms 2_0da0f78f-cd68-48d5-8070-b71070bed549.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'plain-human-head-in-left-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('plain', 'human', 'head', 'in', 'left', 'profile')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        def p(x,y):return (48-x,y) if False else (x,y)
        path('profile',p(32,44),[('C',p(34,30),p(29,37),p(32,34)),('C',p(40,18),p(38,25),p(40,23)),('A',p(26,4),14,14,False),('A',p(12,18),14,14,False),('L',p(8,26)),('L',p(13,27)),('L',p(13,32)),('A',p(18,37),5,5,False),('L',p(23,37)),('L',p(23,44))])
