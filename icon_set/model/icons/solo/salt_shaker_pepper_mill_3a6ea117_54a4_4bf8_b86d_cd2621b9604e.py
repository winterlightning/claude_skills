"""Salt Shaker and Pepper Mill."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a6ea117-54a4-4bf8-b86d-cd2621b9604e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/seasoning pepper_3a6ea117-54a4-4bf8-b86d-cd2621b9604e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'salt-shaker-pepper-mill'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('salt', 'shaker', 'pepper', 'mill')

    def build(self):
        # Plan: Supplied seasoning pair: short capped salt shaker beside tall pepper mill. Neck and cap kept as broad simple silhouettes; small spindle omitted. No useful exact Lucide match.
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

        path('salt',(6,42),[('L',(8,24)),('A',(18,24),5,6,True),('L',(20,42)),('L',(6,42))],True)
        line('cap',(8,24),(18,24));join('cap','salt')
        path('mill',(30,42),[('L',(28,38)),('L',(31,22)),('L',(28,15)),('L',(28,10)),('A',(32,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,15)),('L',(39,22)),('L',(42,38)),('L',(40,42)),('L',(30,42))],True)
        line('collar',(28,15),(42,15));join('collar','mill')
