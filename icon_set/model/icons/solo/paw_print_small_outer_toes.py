'paw-print-small-outer-toes: Four rounded toes in a compact arch above a smooth mirrored three-lobed pad; smaller outlined outer toes. Original redrawn in place after the nine-icon meaning review.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '193cadb3-56bf-56a6-8cdf-a6db99d7d95e'
SOURCE_PATH = 'pictographic-primitives/animals/animal print_193cadb3-56bf-56a6-8cdf-a6db99d7d95e.svg'
AUTHOR = 'gpt-6'

class PawPrintSmallOuterToes(Solo48):
    icon_id = 'paw-print-small-outer-toes'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self):
        # Symbol plan: Four rounded toes in a compact arch above a smooth mirrored three-lobed pad; smaller outlined outer toes.

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
        for n,x,y,rx,ry in [('upper-left',15,8,4,4),('upper-right',33,8,4,4),('outer-left',8,23,3,3),('outer-right',40,23,3,3)]:ellipse(n,x,y,rx,ry)
        path('pad',(24,25),[('C',(18,29),(21,25),(20,26)),('C',(12,38),(16,32),(12,33)),('C',(18,44),(12,42),(14,44)),('C',(24,42),(20,44),(22,42)),('C',(30,44),(26,42),(28,44)),('C',(36,38),(34,44),(36,42)),('C',(30,29),(36,33),(32,32)),('C',(24,25),(28,26),(27,25))],True)
