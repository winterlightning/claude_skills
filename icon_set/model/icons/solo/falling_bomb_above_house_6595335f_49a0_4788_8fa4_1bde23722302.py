"""Falling Bomb Above House
Plan: A small diagonal falling bomb sits upper-left above the house roof.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide bomb: compact shell, house uses clear pitched roof.
Reduction: Omitted tiny motion dash and house door to preserve separation.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6595335f-49a0-4788-8fa4-1bde23722302'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/refugee immigration war 1_6595335f-49a0-4788-8fa4-1bde23722302.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'falling-bomb-above-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bomb', 'house', 'war', 'airstrike', 'building', 'conflict')

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
        path('bomb',(6,6),[('L',(14,8)),('L',(18,12)),('A',(12,18),5,5,True),('L',(8,14)),('L',(6,6))],True)
        self.add_polyline('house',(18,30),(30,20),(42,30),(42,42),(18,42),closed=True)
