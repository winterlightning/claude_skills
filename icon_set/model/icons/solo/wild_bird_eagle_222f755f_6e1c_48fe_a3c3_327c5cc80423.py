'perched-bird: Restore a hooked beak, eye, folded wing and a visible branch beneath the bird. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '222f755f-6e1c-48fe-a3c3-327c5cc80423'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird eagle_222f755f-6e1c-48fe-a3c3-327c5cc80423.svg'
AUTHOR = 'gpt-6'


class PerchedBird(Solo48):
    icon_id = 'perched-bird'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bird', 'perched', 'standing', 'beak', 'wing', 'legs', 'wildlife', 'simple')

    def build(self):
        # Symbol plan: Restore a hooked beak, eye, folded wing and a visible branch beneath the bird.

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
        path('bird',(16,18),[('L',(16,12)),('A',(36,12),10,8,True),('L',(42,18)),('L',(34,20)),('C',(32,32),(33,22),(36,28)),('C',(16,34),(29,36),(17,36)),('L',(6,34)),('C',(16,18),(6,26),(11,19))],True)
        path('wing',(16,18),[('C',(16,34),(25,21),(24,31))]);join('wing','bird')
        dot('eye',(26,13));line('leg',(24,36),(24,44));line('branch',(10,44),(38,44));join('leg','bird');join('leg','branch')
