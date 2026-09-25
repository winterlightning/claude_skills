"""Chicken Drumstick with Bitten Upper Edge
Plan: Diagonal drumstick widens from the bone at lower-left to bitten meat at upper-right.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide drumstick: distinct bone and broad meaty end.
Reduction: Reduced three shallow bite scallops to two broad concavities; retained bone nub.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a208e68-7ddc-4cbb-b3ca-7480f19c88c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/drumstick bite_9a208e68-7ddc-4cbb-b3ca-7480f19c88c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chicken-drumstick-with-bitten-upper-edge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('drumstick', 'chicken', 'bite', 'bone', 'food', 'meat', 'poultry')

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
        path('drumstick',(6,35),[('C',(14,29),(6,29),(10,32)),('C',(24,6),(16,17),(15,6)),('L',(35,6)),('C',(35,17),(30,10),(30,17)),('C',(42,24),(35,23),(38,25)),('C',(20,34),(35,33),(27,28)),('L',(15,40)),('C',(10,42),(15,42),(12,42)),('C',(6,35),(6,42),(6,39))],True)
