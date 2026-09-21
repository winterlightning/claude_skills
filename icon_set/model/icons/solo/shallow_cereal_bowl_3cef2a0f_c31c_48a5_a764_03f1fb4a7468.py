"""Shallow Cereal Bowl
Plan: Wide oval opening above a rounded bowl body; a single food mark is centered in the opening.
Keyshape HRECT_M: (2, 8, 46, 40).
Construction reference: Lucide soup: simple bowl and broad negative space.
Reduction: Reduced cereal marks to one short dash; retained oval perspective.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cef2a0f-c31c-48a5-a764-03f1fb4a7468'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/breakfast cereal bowl_3cef2a0f-c31c-48a5-a764-03f1fb4a7468.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shallow-cereal-bowl'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('cereal', 'bowl', 'breakfast', 'food', 'dish', 'meal', 'kitchen')

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
        path('rim',(4,20),[('A',(44,20),20,10,True),('A',(4,20),20,10,True)],True)
        path('body',(44,20),[('C',(24,38),(42,33),(35,38)),('C',(4,20),(13,38),(6,33))])
        for r in ['rim-0','rim-1']:
            self.relate('connect','body-0',r);self.relate('connect','body-1',r)
        self.add_line('cereal',(23,20),(25,20))
