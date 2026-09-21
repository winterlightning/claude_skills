"""Broad Circular Ring with Empty Center
Plan: Two concentric circles about one center
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: No useful Lucide match; simple circular construction.
Reduction: Preserve broad empty ring."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '558eb953-d4fe-4cd7-a2a4-76aed0a8c4f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/square ring_558eb953-d4fe-4cd7-a2a4-76aed0a8c4f5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-circular-ring-with-empty-center'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ring', 'circle', 'band', 'round', 'shape', 'outline')

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
        circle('outer',24,24,20)
        circle('inner',24,24,11)
