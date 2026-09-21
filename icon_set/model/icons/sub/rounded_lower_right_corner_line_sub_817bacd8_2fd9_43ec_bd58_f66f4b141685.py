"""Rounded Lower Right Corner Line
Plan: An open lower-right corner with one rounded turn.
Keyshape SQUARE: (0, 0, 32, 32).
Construction reference: Lucide file: tangent quarter-circle corner.
Reduction: Complete reference retained; routed to icon-sub because this is a reusable corner mark.."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '817bacd8-2fd9-43ec-bd58-f66f4b141685'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/move bottom right_817bacd8-2fd9-43ec-bd58-f66f4b141685.svg'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'rounded-lower-right-corner-line-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives/shape'
    aliases = ()
    keywords = ('corner', 'right', 'bottom', 'line', 'border', 'angle', 'geometry')

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
        path('corner',(2,30),[('L',(26,30)),('A',(30,26),4,4,False),('L',(30,2))])
