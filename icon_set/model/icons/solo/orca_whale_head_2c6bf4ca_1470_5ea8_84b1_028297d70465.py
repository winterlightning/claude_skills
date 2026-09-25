'orca-head: Restore a rounded snout, swept dorsal profile, oval eye patch and curved white lower jaw boundary. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c6bf4ca-1470-5ea8-84b1-028297d70465'
SOURCE_PATH = 'pictographic-primitives/animals/orca whale head_2c6bf4ca-1470-5ea8-84b1-028297d70465.svg'
AUTHOR = 'gpt-6'


class OrcaHead(Solo48):
    icon_id = 'orca-head'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('orca', 'head')

    def build(self):
        # Symbol plan: Restore a rounded snout, swept dorsal profile, oval eye patch and curved white lower jaw boundary.

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
        path('orca',(4,24),[('C',(30,12),(10,10),(22,6)),('L',(40,8)),('C',(40,28),(35,16),(38,21)),('L',(44,40)),('C',(4,24),(24,38),(12,36))],True)
        line('eye-patch',(20,18),(24,18))
        path('jaw',(4,24),[('C',(28,36),(14,24),(24,28))]);join('jaw','orca')
