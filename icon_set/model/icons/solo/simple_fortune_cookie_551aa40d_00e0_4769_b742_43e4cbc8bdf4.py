"""Simple Fortune Cookie."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '551aa40d-00e0-4769-b742-43e4cbc8bdf4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fortune cookies_551aa40d-00e0-4769-b742-43e4cbc8bdf4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-fortune-cookie'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('simple', 'fortune', 'cookie')

    def build(self):
        # Plan: Fortune cookie shell with a deep right-side notch and attached inner crease. Two folded ends remain broad; deliberate directional asymmetry. No useful exact Lucide match.
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

        path('cookie',(24,6),[('C',(42,22),(34,6),(42,14)),('C',(27,25),(42,29),(34,29)),('L',(39,37)),('C',(25,42),(43,42),(32,42)),('C',(6,25),(13,42),(6,35)),('C',(24,6),(6,15),(15,6))],True)
        line('crease',(21,18),(27,25));join('crease','cookie')
