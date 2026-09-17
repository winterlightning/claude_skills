"""Simple Fish Profile."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d55e699-c6f8-4291-a4f4-179e41bf0474'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/salmon_4d55e699-c6f8-4291-a4f4-179e41bf0474.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-fish-profile'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('simple', 'fish', 'profile')

    def build(self):
        # Plan: Left-facing fish with a rounded head, tapered body and forked tail. Lucide fish informs coherent curved body and eye placement; the crowded gill line is omitted. Directional asymmetry is intentional.
        # Envelope: HRECT_M; visible ink (2, 8, 46, 40) on SOLO48.

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

        path('fish',(4,24),[('C',(17,10),(4,16),(9,10)),('C',(30,24),(24,10),(27,18)),('L',(44,12)),('C',(40,24),(41,16),(40,19)),('C',(44,36),(40,29),(41,32)),('L',(30,24)),('C',(17,38),(27,30),(24,38)),('C',(4,24),(9,38),(4,32))],True)
        self.add_dot('eye',(14,24))
