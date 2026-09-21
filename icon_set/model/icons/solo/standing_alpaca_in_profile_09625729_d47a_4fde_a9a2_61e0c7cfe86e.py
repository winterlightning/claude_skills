"""Standing Alpaca in Profile
Plan: Right-facing alpaca with upright neck, ear and rounded muzzle.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Four overlapping legs reduced to two visible legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09625729-d47a-4fde-a9a2-61e0c7cfe86e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/alpaca_09625729-d47a-4fde-a9a2-61e0c7cfe86e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-alpaca-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('alpaca', 'animal', 'camelid', 'livestock', 'profile', 'legs', 'neck')

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
        path('alpaca',(6,25),[('A',(12,19),6,6,True),('L',(24,19)),('L',(24,12)),('L',(31,6)),('L',(33,14)),('L',(39,16)),('A',(42,19),3,3,True),('C',(39,25),(42,22),(42,25)),('L',(34,25)),('L',(36,42)),('L',(26,42)),('L',(25,31)),('L',(17,31)),('L',(14,42)),('L',(6,42)),('L',(8,31)),('C',(6,25),(6,30),(6,28))],True)
