"""Taco with Salsa and Drink."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6eb4d767-9381-481d-8f4a-4d7d28edd08c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear tacos_6eb4d767-9381-481d-8f4a-4d7d28edd08c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'taco-salsa-pepper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('taco', 'salsa', 'pepper')

    def build(self):
        # Plan: Folded taco shell with a small salsa bowl above and a curved pepper to the right. Natural food group retains all three subjects. Shell layers reduced to one clear half-oval and pepper details omitted at 48 pixels. No useful exact Lucide match.
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

        path('taco',(6,22),[('A',(6,42),18,10,True),('L',(6,22))],True)
        path('salsa',(24,6),[('L',(42,6)),('A',(24,6),9,9,True)],True)
        path('pepper',(42,24),[('C',(34,42),(42,34),(40,42)),('C',(34,30),(34,42),(34,36)),('L',(42,24))],True)
