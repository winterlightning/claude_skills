"""Three Node Branch Junction
Plan: Three circular nodes meet at a central fork; the right nodes mirror vertically.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide git-fork: circular terminals and sparse joining branches.
Reduction: No omitted nodes.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ad1f13c-d23e-4783-a465-9f43c1ac5b56'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/code branch_3ad1f13c-d23e-4783-a465-9f43c1ac5b56.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-node-branch-junction'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    aliases = ()
    keywords = ('nodes', 'branch', 'junction', 'network', 'connections', 'diagram', 'three')

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
        circle('left',9,24,5);circle('upper',39,13,5);circle('lower',39,35,5)
        self.add_line('stem',(14,24),(23,24))
        self.add_line('upper-branch',(23,24),(34,13));self.add_line('lower-branch',(23,24),(34,35))
        for m in ['left-1','left-2']:self.relate('connect','stem',m)
        for name in ['upper','lower']:
            for m in [name+'-0',name+'-3']:self.relate('connect',name+'-branch',m)
            self.relate('connect','stem',name+'-branch')
        self.relate('connect','upper-branch','lower-branch')
