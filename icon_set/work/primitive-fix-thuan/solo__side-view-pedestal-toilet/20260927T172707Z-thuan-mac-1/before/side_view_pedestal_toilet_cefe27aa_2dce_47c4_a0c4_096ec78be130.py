"""Side View Pedestal Toilet
Plan: Side-view cistern, broad seat, curved bowl and pedestal.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide toilet: continuous bowl and broad stable foot.
Reduction: Tank band and second seat line omitted; shared seat seam drawn only once.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cefe27aa-2dce-47c4-a0c4-096ec78be130'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bidet_cefe27aa-2dce-47c4-a0c4-096ec78be130.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-pedestal-toilet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('toilet', 'bathroom', 'cistern', 'bowl', 'plumbing', 'pedestal', 'restroom')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        path('cistern',(6,26),[('L',(6,9)),('A',(9,6),3,3,True),('L',(15,6)),('A',(18,9),3,3,True),('L',(18,26))])
        path('bowl',(6,26),[('L',(42,26)),('C',(32,34),(42,31),(38,33)),('L',(32,42)),('L',(16,42)),('L',(16,34)),('C',(6,26),(11,33),(6,31))],True);self.relate('connect','bowl','cistern')
