"""Simple Mushroom Symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a015da24-e348-5b62-9335-0c666e6cfda5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mushroom_a015da24-e348-5b62-9335-0c666e6cfda5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-rounded-mushroom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('simple', 'rounded', 'mushroom')

    def build(self):
        # Plan: Broad rounded mushroom cap above a flared central stem. Shared bilateral cap and stem nodes; no surface decoration. No useful exact Lucide match.
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

        path('cap',(6,25),[('C',(24,6),(6,15),(14,6)),('C',(42,25),(34,6),(42,15)),('A',(39,28),3,3,True),('L',(30,26)),('L',(18,26)),('L',(9,28)),('A',(6,25),3,3,True)],True)
        path('stem',(18,26),[('L',(16,37)),('C',(24,42),(15,42),(20,42)),('C',(32,37),(28,42),(33,42)),('L',(30,26))]);join('stem','cap')
