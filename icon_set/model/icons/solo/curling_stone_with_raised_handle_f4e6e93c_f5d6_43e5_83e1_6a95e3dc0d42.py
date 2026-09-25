"""Curling Stone with Raised Handle
Plan: Rounded stone with middle seam and raised handle
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: No useful Lucide match; shared rounded body.
Reduction: Use one handle stroke and retain stone band."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4e6e93c-f5d6-43e5-83e1-6a95e3dc0d42'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/curler_f4e6e93c-f5d6-43e5-83e1-6a95e3dc0d42.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curling-stone-with-raised-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curling', 'stone', 'handle', 'sport', 'ice', 'equipment', 'game')

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
        rect('stone',4,20,40,20,8)
        self.add_line('band',(4,30),(44,30));self.relate('connect','band','stone')
        path('handle',(18,20),[('L',(18,12)),('A',(22,8),4,4,True),('L',(34,8))]);self.relate('connect','handle','stone')
