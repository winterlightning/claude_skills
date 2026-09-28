"""Spiky Durian Fruit."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6aba0722-424b-4f5e-95ea-9f8fc1a40e2c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/durian_6aba0722-424b-4f5e-95ea-9f8fc1a40e2c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiky-durian-fruit'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('spiky', 'durian', 'fruit')

    def build(self):
        # Plan: Upright durian with a short stem and broad triangular spikes. Mirrored polygon around central axis; fewer spikes preserve open valleys. No useful exact Lucide match.
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

        poly('fruit',(24,10),(30,16),(38,12),(36,23),(40,28),(35,33),(36,42),(28,39),(24,44),(20,39),(12,42),(13,33),(8,28),(12,23),(10,12),(18,16),(24,10),closed=True)
        line('stem',(24,4),(24,10));join('stem','fruit')
