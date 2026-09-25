"""Plain Short-Sleeved T-Shirt
Plan: Mirrored short sleeves, scoop neckline and rounded hem.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide shirt: connected garment outline.
Reduction: Secondary collar seam omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f08146a9-794d-4857-8533-8d73e32d7f26'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/apparel_f08146a9-794d-4857-8533-8d73e32d7f26.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-short-sleeved-t-shirt'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('t-shirt', 'shirt', 'clothing', 'sleeves', 'collar', 'apparel', 'garment')

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
        path('shirt',(16,6),[('A',(32,6),8,8,False),('L',(36,8)),('L',(42,18)),('L',(35,24)),('L',(33,21)),('L',(33,39)),('A',(30,42),3,3,True),('L',(18,42)),('A',(15,39),3,3,True),('L',(15,21)),('L',(13,24)),('L',(6,18)),('L',(12,8)),('L',(16,6))],True)
