"""Two Cavity Concrete Block
Plan: Rounded block with paired rectangular cavities
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: No useful Lucide match; shared rectangular grid.
Reduction: Keep both cavities; no texture."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f20bf364-b592-4325-9e9e-a9ef6996da39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/concrete_f20bf364-b592-4325-9e9e-a9ef6996da39.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-cavity-concrete-block'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('concrete', 'block', 'cinder', 'cavities', 'construction', 'masonry', 'building')

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
        rect('block',4,8,40,32)
        rect('left',12,16,8,16)
        rect('right',28,16,8,16)
