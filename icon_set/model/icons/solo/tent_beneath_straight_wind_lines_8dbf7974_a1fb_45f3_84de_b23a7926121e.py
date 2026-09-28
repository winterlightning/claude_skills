"""Tent beneath Straight Wind Lines
Plan: Triangular tent beneath two detached wind strokes.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide tent: coherent triangle and entry.
Reduction: Small triangular opening replaced by the closed tent door seam; natural outdoor weather scene retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dbf7974-a1fb-45f3-84de-b23a7926121e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camping tent small_8dbf7974-a1fb-45f3-84de-b23a7926121e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tent-beneath-straight-wind-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tent', 'wind', 'camping', 'outdoors', 'entrance', 'weather', 'scene')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        self.add_line('wind-1',(12,6),(36,6));self.add_line('wind-2',(6,14),(36,14))
        self.add_polyline('tent',(6,42),(24,23),(42,42),closed=True)
        self.add_line('door-seam',(24,23),(24,42));self.relate('connect','tent','door-seam')
