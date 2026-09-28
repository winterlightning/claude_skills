"""Sliced Fig Fruit."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '410e1401-f431-559e-8af7-0c0bab602a85'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fig slice_410e1401-f431-559e-8af7-0c0bab602a85.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sliced-fig-fruit'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('sliced', 'fig', 'fruit')

    def build(self):
        # Plan: Pear-shaped fig section with a short thick stem and a teardrop cavity. Bilateral construction; tiny cavity seed marks omitted because the inner chamber cannot hold another detail level. No useful exact Lucide match.
        # Envelope: VRECT_M; visible ink (8, 2, 40, 46) on SOLO48.

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

        path('fig',(20,4),[('L',(28,4)),('L',(28,10)),('C',(38,29),(28,16),(38,20)),('C',(24,44),(38,39),(33,44)),('C',(10,29),(15,44),(10,39)),('C',(20,10),(10,20),(20,16)),('L',(20,4))],True)
        path('cavity',(24,21),[('C',(29,30),(26,23),(29,26)),('C',(24,35),(29,33),(27,35)),('C',(19,30),(21,35),(19,33)),('C',(24,21),(19,26),(22,23))],True)
