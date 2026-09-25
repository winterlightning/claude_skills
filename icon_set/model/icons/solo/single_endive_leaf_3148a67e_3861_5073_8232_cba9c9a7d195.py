"""Single Wavy Endive Leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3148a67e-3861-5073-8232-cba9c9a7d195'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/endive_3148a67e-3861-5073-8232-cba9c9a7d195.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-endive-leaf'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('single', 'endive', 'leaf')

    def build(self):
        # Plan: Narrow wavy endive with a central vein and paired short branches. Mirrored undulations and shared vein junction. Dense secondary veins omitted; Lucide leaf informs the single central stroke.
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

        path('leaf',(24,44),[('C',(15,34),(18,44),(15,39)),('C',(10,26),(15,30),(10,31)),('C',(12,18),(10,22),(12,22)),('C',(17,10),(12,12),(13,10)),('C',(24,4),(21,10),(20,4)),('C',(31,10),(28,4),(27,10)),('C',(36,18),(35,10),(36,12)),('C',(38,26),(36,22),(38,22)),('C',(33,34),(38,31),(33,30)),('C',(24,44),(33,39),(30,44))],True)
        poly('vein',(24,44),(24,30),(24,16));join('vein','leaf')
        poly('branches',(19,24),(24,30),(29,24));join('branches','vein')
