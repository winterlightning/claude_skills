'Stacking ring toy.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11f12d81-7f9c-589f-99c1-4d862f93acd8'
SOURCE_PATH = 'pictographic-primitives/babies/toy_11f12d81-7f9c-589f-99c1-4d862f93acd8.svg'
AUTHOR = 'gpt-6'

class StackingRingToy(Solo48):
    icon_id = 'stacking-ring-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('stacking', 'ring', 'toy', 'infant', 'nursery')

    def build(self):
        # Reduced the toy to two rounded stacking rings and one central peg.

        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('peg',(18,18),[('L',(18,12)),('A',(24,6),6,6,True),('A',(30,12),6,6,True),('L',(30,18))])
        path('upper',(18,18),[('L',(30,18)),('A',(36,24),6,6,True),('A',(30,30),6,6,True),('L',(18,30)),('A',(12,24),6,6,True),('A',(18,18),6,6,True)],True)
        path('lower',(12,30),[('L',(18,30)),('L',(30,30)),('L',(36,30)),('A',(42,36),6,6,True),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('A',(12,30),6,6,True)],True)
        join('peg','upper');join('upper','lower')
