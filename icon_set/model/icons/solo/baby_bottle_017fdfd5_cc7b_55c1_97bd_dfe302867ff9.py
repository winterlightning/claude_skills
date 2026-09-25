'baby-bottle: Narrow feeding bottle with a projecting teat, collar and two measurement ticks. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '017fdfd5-cc7b-55c1-97bd-dfe302867ff9'
SOURCE_PATH = 'pictographic-primitives/babies/baby care bottle_017fdfd5-cc7b-55c1-97bd-dfe302867ff9.svg'
AUTHOR = 'gpt-6'

class BabyBottle(Solo48):
    icon_id = 'baby-bottle'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('bottle', 'baby', 'milk', 'feeding', 'teat', 'infant', 'formula', 'nursing')

    def build(self):
        # Symbol plan: Narrow feeding bottle with a projecting teat, collar and two measurement ticks.

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
        path('bottle',(16,20),[('L',(12,24)),('L',(12,40)),('A',(16,44),4,4,False),('L',(32,44)),('A',(36,40),4,4,False),('L',(36,24)),('L',(32,20)),('L',(16,20))],True)
        path('teat',(16,20),[('L',(16,14)),('C',(20,8),(16,12),(20,12)),('A',(28,8),4,4,True),('C',(32,14),(28,12),(32,12)),('L',(32,20))])
        join('bottle','teat')
        line('measure-1',(12,28),(20,28));line('measure-2',(12,36),(20,36))
        join('measure-1','bottle');join('measure-2','bottle')
