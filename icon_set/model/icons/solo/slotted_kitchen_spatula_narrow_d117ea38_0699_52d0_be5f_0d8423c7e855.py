"""Slotted Kitchen Spatula."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd117ea38-0699-52d0-be5f-0d8423c7e855'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/spatula_d117ea38-0699-52d0-be5f-0d8423c7e855.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slotted-kitchen-spatula-narrow'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('slotted', 'kitchen', 'spatula', 'narrow')

    def build(self):
        # Plan: Narrow spatula head with two vertical slots and a longer handle. Repeated slots and rounded head share dimensions. Outlined handle simplified to a single stroke. No useful exact Lucide match.
        # Envelope: VRECT_M; visible ink (8, 2, 40, 46) on SOLO48.

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

        path('head',(14,4),[('L',(34,4)),('A',(38,8),4,4,True),('L',(38,20)),('A',(34,24),4,4,True),('L',(24,24)),('L',(14,24)),('A',(10,20),4,4,True),('L',(10,8)),('A',(14,4),4,4,True)],True)
        line('handle',(24,24),(24,44));join('head','handle')
        for j,x in enumerate((19,29)):line('slot-'+str(j),(x,13),(x,15))
