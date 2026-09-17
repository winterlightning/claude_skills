"""Symmetrical Leafy Plant Stem."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68045b9b-2507-5683-af49-876506f90549'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/wasabi plant_68045b9b-2507-5683-af49-876506f90549.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'symmetrical-leafy-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('symmetrical', 'leafy', 'plant')

    def build(self):
        # Plan: Symmetrical plant with a pointed top leaf, two broad lower leaves and two upper shoots. Shared stem, mirrored side leaves and shared shoot node. Lucide leaf and wheat inform the construction; upper leaf outlines reduced to open shoots to preserve the two-tier silhouette and clear gaps.
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

        poly('stem',(24,44),(24,40),(24,22),(24,12))
        path('top',(24,4),[('C',(24,12),(16,5),(16,11)),('C',(24,4),(32,11),(32,5))],True);join('top','stem')
        path('left-leaf',(24,40),[('C',(8,28),(12,40),(8,36)),('C',(24,40),(18,28),(24,32))],True)
        path('right-leaf',(24,40),[('C',(40,28),(36,40),(40,36)),('C',(24,40),(30,28),(24,32))],True)
        join('left-leaf','stem');join('right-leaf','stem')
        poly('upper-shoots',(8,18),(24,22),(40,18));join('upper-shoots','stem')
