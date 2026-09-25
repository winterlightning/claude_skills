"""Blueberry with Star Crown
Plan: Round berry with five-point crown.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide leaf: pointed botanical detail.
Reduction: Tiny crown dash omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e4ccf93-b285-4559-b913-7321ca7f0263'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blueberry_4e4ccf93-b285-4559-b913-7321ca7f0263.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blueberry-with-star-crown'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('blueberry', 'berry', 'fruit', 'crown', 'food', 'produce', 'plant')

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
        path('berry',(13,17),[('C',(8,30),(9,19),(8,25)),('A',(24,44),16,14,False),('A',(40,30),16,14,False),('C',(35,17),(40,25),(39,19))])
        self.add_polyline('crown',(13,17),(10,9),(20,12),(24,4),(28,12),(38,9),(35,17),(32,23),(24,19),(16,23),(13,17))
        self.relate('connect','berry','crown')
