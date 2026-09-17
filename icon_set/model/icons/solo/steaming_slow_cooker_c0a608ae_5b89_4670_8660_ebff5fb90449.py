"""Steaming Slow Cooker."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0a608ae-5b89-4670-8660-ebff5fb90449'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/slow cooker_c0a608ae-5b89-4670-8660-ebff5fb90449.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-slow-cooker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('steaming', 'slow', 'cooker')

    def build(self):
        # Plan: Slow cooker with a domed lid, central knob, front control dot and two steam curls. Lucide cooking-pot informs the rounded body and shared rim. Circular dial reduced to a dot and third steam trail removed to preserve spacing. Steam curves mirror around the central axis.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(6,24),[('L',(42,24)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,24))],True)
        path('lid',(6,24),[('C',(24,14),(8,16),(16,14)),('C',(42,24),(32,14),(40,16))]);join('lid','body')
        line('knob',(24,10),(24,14));join('knob','lid')
        self.add_dot('control',(24,33))
        for j,x in enumerate((8,40)):
            direction=1 if j==0 else -1
            path('steam-'+str(j),(x,6),[('C',(x,8),(x-2*direction,6),(x+2*direction,8))])
