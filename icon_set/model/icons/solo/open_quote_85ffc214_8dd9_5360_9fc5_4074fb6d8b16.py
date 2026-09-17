'open-quote: Use two clearly open quotation marks with rounded lower bowls and sweeping upper hooks. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85ffc214-8dd9-5360-9fc5-4074fb6d8b16'
SOURCE_PATH = 'pictographic-primitives/interface-essential/open quote_85ffc214-8dd9-5360-9fc5-4074fb6d8b16.svg'
AUTHOR = 'gpt-6'

class OpenQuote(Solo48):
    icon_id = 'open-quote'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('open', 'quote', 'interface-essential')

    def build(self):
        # Symbol plan: Use two clearly open quotation marks with rounded lower bowls and sweeping upper hooks.

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
        for n,x in [('left',4),('right',28)]:
         path(n,(x+14,10),[('C',(x,24),(x+4,10),(x,16)),('L',(x,38)),('L',(x+7,38)),('A',(x+7,24),7,7,False)])
