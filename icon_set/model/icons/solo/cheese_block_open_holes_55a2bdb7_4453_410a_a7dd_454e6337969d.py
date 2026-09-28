"""Cheese Block with Open Holes
Plan: Broad cheese block with two edge cutouts and three interior holes.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: No useful exact Lucide match; smooth rectangular outline with concave notches.
Reduction: Chips represented by two small circles and one dot; edge bites retain their hierarchy.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55a2bdb7-4453-410a-a7dd-454e6337969d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nougat_55a2bdb7-4453-410a-a7dd-454e6337969d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cheese-block-open-holes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cheese', 'block', 'holes', 'dairy', 'food', 'swiss')

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
        path('cheese',(4,8),[('L',(44,8)),('L',(44,16)),('L',(37,16)),('A',(37,24),4,4,False),('L',(44,24)),('L',(44,32)),('A',(44,40),4,4,False),('L',(4,40)),('L',(4,8))],True)
        circle('hole-top',16,20,3)
        self.add_dot('hole-left',(13,31));self.add_dot('hole-right',(25,31))
