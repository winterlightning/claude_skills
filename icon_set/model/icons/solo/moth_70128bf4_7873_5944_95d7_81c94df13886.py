'moth: Show the broad triangular forewings, lower wing lobes, central body and antennae. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70128bf4-7873-5944-95d7-81c94df13886'
SOURCE_PATH = 'pictographic-primitives/animals/moth_70128bf4-7873-5944-95d7-81c94df13886.svg'
AUTHOR = 'gpt-6'


class Moth(Solo48):
    icon_id = 'moth'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('moth', 'animal')

    def build(self):
        # Symbol plan: Show the broad triangular forewings, lower wing lobes, central body and antennae.

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
        path('wings',(24,18),[('C',(6,12),(18,18),(12,12)),('L',(6,34)),('C',(14,38),(6,40),(10,42)),('L',(24,30)),('L',(34,38)),('C',(42,34),(38,42),(42,40)),('L',(42,12)),('C',(24,18),(36,12),(30,18))],True)
        line('body',(24,18),(24,42));poly('antennae',(16,6),(24,18),(32,6))
        join('wings','body');join('wings','antennae');join('body','antennae')
