"""Serving Tray with Cloche."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55dd0201-a9b1-475a-ad26-32ecd334e13f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/tools kitchen serving dome_55dd0201-a9b1-475a-ad26-32ecd334e13f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'serving-tray-cloche'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('serving', 'tray', 'cloche')

    def build(self):
        # Plan: Serving dome on a shallow tray with an attached top knob. Mirror axis 24, shared dome/tray nodes. Lucide cooking-pot informs the tray rim and rounded lower corners; circular knob reduced to a stem.
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

        path('dome',(8,30),[('A',(24,14),16,16,True),('A',(40,30),16,16,True)])
        path('tray',(4,30),[('L',(8,30)),('L',(40,30)),('L',(44,30)),('L',(40,37)),('A',(35,40),6,6,True),('L',(13,40)),('A',(8,37),6,6,True),('L',(4,30))],True);join('dome','tray')
        line('knob',(24,8),(24,14));join('knob','dome')
