'nearly-full-battery: Restore a low battery silhouette, attached terminal and three equal charge bars with one empty slot. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fb93b96-e635-44d6-a1a9-9d8b92459ec7'
SOURCE_PATH = 'pictographic-primitives/mobile/charging battery almost full_4fb93b96-e635-44d6-a1a9-9d8b92459ec7.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'nearly-full-battery'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/mobile"
    aliases = ()
    keywords = ('battery', 'charge', 'level', 'nearly-full', 'power', 'energy', 'indicator')

    def build(self):
        # Symbol plan: Restore a low battery silhouette, attached terminal and three equal charge bars with one empty slot.

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
        rounded('battery',2,12,42,36,4)
        line('terminal',(42,24),(46,24));join('terminal','battery')
        for x in (11,19,27):line('charge-'+str(x),(x,21),(x,27))
