"""Arched-Handle Shopping Basket
Plan: Arched handle, broad rim and tapered bowl.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide shopping-basket: taper and rim relationship.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb339077-43d0-4a73-bbbe-2861fc08dcbf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/pannier_bb339077-43d0-4a73-bbbe-2861fc08dcbf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapered-basket-arched-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('basket', 'shopping', 'handle', 'container', 'market', 'carry')

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
        path('handle',(14,22),[('L',(14,16)),('A',(34,16),10,10,True),('L',(34,22))])
        rect('rim',6,22,36,8,4)
        path('basket',(9,30),[('L',(13,39)),('C',(17,42),(14,41),(15,42)),('L',(31,42)),('C',(35,39),(33,42),(34,41)),('L',(39,30))])
        self.relate('connect','handle','rim');self.relate('connect','basket','rim')
