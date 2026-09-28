"""Smooth circular cranium, rounded chin and continuous neck; retain source facing direction and open neck base.
Construction: Human reference user.svg: circular head vocabulary; continuous-neck source profile, no detached gap.
Omissions: Fine lip serrations omitted to avoid crowded strokes.
Keyshape VRECT_L: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9d91410d-5cf6-45ea-9b33-64ea070b4ce4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plain-head-profile/20260924T111035Z-thuan-mac/reference/head side_9d91410d-5cf6-45ea-9b33-64ea070b4ce4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'plain-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('plain', 'head', 'profile')
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

        def p(x,y):return (48-x,y) if True else (x,y)
        path('profile',p(32,44),[('C',p(34,30),p(29,37),p(32,34)),('C',p(40,18),p(38,25),p(40,23)),('A',p(26,4),14,14,True),('A',p(12,18),14,14,True),('L',p(8,26)),('L',p(13,27)),('L',p(13,32)),('A',p(18,37),5,5,True),('L',p(23,37)),('L',p(23,44))])
