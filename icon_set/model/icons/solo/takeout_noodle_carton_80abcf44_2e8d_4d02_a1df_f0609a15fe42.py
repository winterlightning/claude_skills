"""Takeout Noodle Box with Chopsticks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80abcf44-2e8d-4d02-a1df-f0609a15fe42'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pasta noodles_80abcf44-2e8d-4d02-a1df-f0609a15fe42.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'takeout-noodle-carton'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('takeout', 'noodle', 'carton')

    def build(self):
        # Plan: Takeout noodle carton under two horizontal chopsticks with two hanging noodle strands. Shared noodle/rim junctions. Interior wave omitted to preserve carton space; no useful exact Lucide match.
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

        poly('carton',(8,24),(20,24),(28,24),(40,24),(36,42),(12,42),(8,24),closed=True)
        for j,y in enumerate((6,14)):poly('chopstick-'+str(j),(6,y),(20,y),(28,y),(42,y))
        for j,x in enumerate((20,28)):
         poly('noodle-'+str(j),(x,6),(x,14),(x,24));join('noodle-'+str(j),'carton');join('noodle-'+str(j),'chopstick-0');join('noodle-'+str(j),'chopstick-1')
