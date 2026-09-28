# Review candidate; original preserved.
"""mosquito: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0145bda3-5e60-4e2f-b201-09ab64a9f332'
SOURCE_PATH = 'pictographic-primitives/animals/dragonfly_0145bda3-5e60-4e2f-b201-09ab64a9f332.svg'
AUTHOR = 'gpt-6'

class Mosquito(Solo48):
    icon_id = 'mosquito'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('mosquito', 'insect', 'bug', 'wings', 'pest', 'bite', 'fly', 'antennae')

    def build(self):
        # Symbol plan: Add a long proboscis and bent paired legs to an elongated insect body, with two broad wings.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        circle('head',24,10,3);line('proboscis',(24,2),(24,7));join('proboscis','head')
        line('body',(24,13),(24,44));join('body','head')
        for n,sign in [('left',-1),('right',1)]:
         def p(x,y):return (24+sign*x,y)
         path(n+'-wing',(24,22),[('C',p(20,16),p(10,20),p(20,10)),('C',(24,22),p(20,24),p(10,25))],True)
         poly(n+'-leg',(24,30),p(12,36),p(18,44))
         join(n+'-wing','body');join(n+'-leg','body')
        join('left-wing','right-wing');join('left-leg','right-leg')
