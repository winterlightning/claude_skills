"""Bird Resting in Nest
Plan: A left-facing bird sits atop a deep semicircular nest. Bird and nest share two endpoints at the rim.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide bird and soup: unified bird outline above a bowl silhouette.
Reduction: Reduced nest layers to one broad bowl; omitted tiny eye.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ee71767-8c7b-4b67-8c9c-982b7a27e635'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nestling_8ee71767-8c7b-4b67-8c9c-982b7a27e635.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bird-resting-in-nest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('bird', 'nest', 'nesting', 'wildlife', 'animal', 'nature')

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
        path('bird',(14,24),[('C',(10,14),(10,20),(10,16)),('L',(4,12)),('L',(13,12)),('A',(29,12),8,4,True),('C',(34,14),(29,15),(30,16)),('L',(40,8)),('L',(36,24))])
        path('nest',(4,24),[('L',(14,24)),('L',(36,24)),('L',(44,24)),('A',(4,24),20,16,True)],True)
        self.relate('connect','bird-0','nest-0');self.relate('connect','bird-0','nest-1')
        self.relate('connect','bird-6','nest-1');self.relate('connect','bird-6','nest-2')
