"""Stalk of Rye Grain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e4b7e57-5225-536a-b5d3-a9451f3d7599'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/rye_0e4b7e57-5225-536a-b5d3-a9451f3d7599.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rye-grain-stalk'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('rye', 'grain', 'stalk')

    def build(self):
        # Plan: Upright rye with one mirrored pair of pointed side grains, one top grain and a straight stem. Lucide wheat informs the grain attachments. Five grains reduced to three large grains so the curved lobes remain open at 48 pixels.
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

        poly('stem',(24,44),(24,38),(24,18))
        path('top-grain',(24,4),[('C',(24,18),(14,10),(14,14)),('C',(24,4),(34,14),(34,10))],True);join('top-grain','stem')
        path('grain-left',(24,38),[('C',(8,26),(12,38),(8,34)),('C',(24,38),(18,26),(24,30))],True)
        path('grain-right',(24,38),[('C',(40,26),(36,38),(40,34)),('C',(24,38),(30,26),(24,30))],True)
        join('grain-left','stem');join('grain-right','stem')
