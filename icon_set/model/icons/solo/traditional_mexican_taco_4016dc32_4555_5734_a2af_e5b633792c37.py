"""Traditional Mexican Taco."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4016dc32-4555-5734-a2af-e5b633792c37'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/food mexican_4016dc32-4555-5734-a2af-e5b633792c37.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'traditional-mexican-taco'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('traditional', 'mexican', 'taco')

    def build(self):
        # Plan: Broad taco shell with a lobed filling visible behind and two shell dots. Shared layer junctions and mirrored curves. Lucide sandwich informs the separated bread and filling layers; smaller shell marks are reduced to dots.
        # Envelope: HRECT_L; visible ink (2, 6, 46, 42) on SOLO48.

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

        path('shell',(4,35),[('C',(8,28),(4,32),(5,30)),('C',(24,20),(12,22),(16,20)),('C',(40,28),(32,20),(36,22)),('C',(44,35),(43,30),(44,32)),('A',(39,40),5,5,True),('L',(9,40)),('A',(4,35),5,5,True)],True)
        path('filling',(8,28),[('C',(14,12),(6,16),(8,12)),('C',(24,8),(18,12),(18,8)),('C',(34,12),(30,8),(30,12)),('C',(40,28),(40,12),(42,16))]);join('filling','shell')
        for j,x in enumerate((20,28)):self.add_dot('texture-'+str(j),(x,31))
