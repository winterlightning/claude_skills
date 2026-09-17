'paw-print-small-outer-toes: Restore a broad three-lobed central paw pad and arrange four toes in an arch, with smaller outer toes. Repaired original in place.'
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
    category = 'nature/animals'
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self):
        # Symbol plan: Restore a broad three-lobed central paw pad and arrange four toes in an arch, with smaller outer toes.

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
        for n,x,y,r in [('upper-left',17,7,3),('upper-right',31,7,3),('outer-left',6,20,2),('outer-right',42,20,2)]:circle(n,x,y,r)

        path('pad',(24,25),[('C',(15,33),(18,25),(19,29)),('C',(12,40),(12,36),(10,38)),('C',(17,44),(12,43),(14,44)),('C',(24,42),(20,44),(21,42)),('C',(31,44),(27,42),(28,44)),('C',(36,40),(34,44),(36,43)),('C',(33,33),(38,38),(36,36)),('C',(24,25),(29,29),(30,25))],True)
