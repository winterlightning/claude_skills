'perching-bird: Restore a rounded breast, pointed beak, visible eye, folded wing and branch instead of a wedge silhouette. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f8fae80-7c30-4fdb-9d48-8b632249f687'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird_0f8fae80-7c30-4fdb-9d48-8b632249f687.svg'
AUTHOR = 'gpt-6'


class PerchingBird(Solo48):
    icon_id = 'perching-bird'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('bird', 'perching', 'songbird', 'wing', 'beak', 'tail', 'garden', 'wildlife')

    def build(self):
        # Symbol plan: Restore a rounded breast, pointed beak, visible eye, folded wing and branch instead of a wedge silhouette.

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
        path('bird',(4,12),[('L',(12,8)),('C',(22,4),(16,4),(18,4)),('C',(30,12),(26,4),(28,8)),('L',(44,36)),('L',(29,34)),('C',(12,24),(18,34),(12,32)),('L',(12,8))])
        path('wing',(22,22),[('C',(26,24),(22,24),(24,24))])
        dot('eye',(21,13))
        line('leg',(23,33),(21,44));line('branch',(10,44),(40,44));join('leg','bird');join('leg','branch')
