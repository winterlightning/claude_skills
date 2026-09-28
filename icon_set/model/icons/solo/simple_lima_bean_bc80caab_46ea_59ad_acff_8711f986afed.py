"""Simple Lima Bean Legume."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc80caab-46ea-59ad-acff-8711f986afed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/lima bean_bc80caab-46ea-59ad-acff-8711f986afed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-lima-bean'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('simple', 'lima', 'bean')

    def build(self):
        # Plan: Smooth kidney-shaped lima bean with a short inner crease. Lucide bean informs the concave shoulder and full outer curve. Organic asymmetry retained.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

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

        path('bean',(30,4),[('C',(40,20),(38,4),(40,12)),('C',(20,44),(40,34),(32,44)),('C',(8,31),(12,44),(8,39)),('C',(20,15),(8,23),(17,22)),('C',(30,4),(23,8),(24,4))],True)
        path('crease',(20,29),[('C',(28,19),(24,27),(27,23))])
