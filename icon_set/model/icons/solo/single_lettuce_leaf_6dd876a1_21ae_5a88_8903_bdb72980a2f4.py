"""Single Lettuce Leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dd876a1-21ae-5a88-8903-bdb72980a2f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/lettuce_6dd876a1-21ae-5a88-8903-bdb72980a2f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-lettuce-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('single', 'lettuce', 'leaf')

    def build(self):
        # Plan: Broad scalloped lettuce leaf with a central vein and one paired branch. Shared vertical axis, mirrored lobes and branch nodes. Thick outlined stalk and second branch pair simplified; Lucide leaf informs the coherent vein.
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

        path('leaf',(24,36),[('C',(14,33),(19,36),(14,37)),('C',(8,26),(14,29),(8,31)),('C',(10,18),(8,22),(10,21)),('C',(15,10),(10,12),(10,10)),('C',(24,4),(20,10),(19,4)),('C',(33,10),(29,4),(28,10)),('C',(38,18),(38,10),(38,12)),('C',(40,26),(38,21),(40,22)),('C',(34,33),(40,31),(34,29)),('C',(24,36),(34,37),(29,36))],True)
        poly('vein',(24,44),(24,36),(24,29),(24,16));join('vein','leaf')
        poly('branches',(18,22),(24,29),(30,22));join('branches','vein')
