'loading-bar: Restore the low horizontal capsule and show a partial progress fill with visible empty space. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a1357f44-093c-4bb6-93d6-7521033c44d2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.svg'
AUTHOR = 'gpt-6'

class LoadingBar(Solo48):
    icon_id = 'loading-bar'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'loading-bar')

    def build(self):
        # Symbol plan: Restore the low horizontal capsule and show a partial progress fill with visible empty space.

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
        path('track',(13,15),[('L',(35,15)),('A',(35,33),9,9,True),('L',(13,33)),('A',(13,15),9,9,True)],True)
        line('progress',(14,24),(28,24))
