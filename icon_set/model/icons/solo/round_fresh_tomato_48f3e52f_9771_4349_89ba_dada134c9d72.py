"""Round Fresh Tomato Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48f3e52f-9771-4349-89ba-dada134c9d72'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/tomato_48f3e52f-9771-4349-89ba-dada134c9d72.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-fresh-tomato'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('round', 'fresh', 'tomato')

    def build(self):
        # Plan: Supplied tomato: round fruit, central leafy calyx and upright stem. Extra leaf tips and lower highlight removed to prevent crowding; bilateral crown and fruit. No useful exact Lucide match.
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

        path('fruit',(10,16),[('C',(6,26),(7,19),(6,22)),('C',(24,42),(6,36),(14,42)),('C',(42,26),(34,42),(42,36)),('C',(38,16),(42,22),(41,19))])
        poly('calyx',(10,16),(16,12),(24,20),(32,12),(38,16));join('calyx','fruit')
        line('stem',(24,6),(24,20));join('stem','calyx')
