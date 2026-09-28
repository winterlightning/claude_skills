"""Stack of Breakfast Pancakes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '799ea4de-0531-534a-9c5e-9d0bf37abe6f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/exotic food oyster_799ea4de-0531-534a-9c5e-9d0bf37abe6f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'breakfast-pancake-stack'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('breakfast', 'pancake', 'stack')

    def build(self):
        # Plan: Three pancake layers with a broad oval top and curved lower edges. Shared side junctions keep the stack coherent. Top marking and separate plate rim omitted to preserve layer spacing. No useful exact Lucide match.
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

        path('top',(4,14),[('A',(44,14),20,6,True),('A',(4,14),20,6,True)],True)
        path('middle',(4,14),[('L',(4,24)),('A',(44,24),20,6,False),('L',(44,14))]);join('middle','top')
        path('bottom',(4,24),[('L',(4,34)),('A',(44,34),20,6,False),('L',(44,24))]);join('bottom','middle')
