"""Standing Partridge Profile
Plan: Right-facing bird with long sloped back, wing, pointed beak and visible leg.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bird: sloping back, rounded breast and thin leg.
Reduction: Wing detail omitted to retain readable body opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '154bf754-2290-4224-b7b5-253cfc6eafb1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/partridge_154bf754-2290-4224-b7b5-253cfc6eafb1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-partridge-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('partridge', 'bird', 'wing', 'tail', 'wildlife', 'standing')

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
        path('bird',(6,34),[('L',(24,16)),('L',(24,14)),('A',(38,14),7,8,True),('L',(42,17)),('L',(37,20)),('L',(37,24)),('C',(25,34),(37,31),(31,34)),('L',(6,34))],True)
        self.add_polyline('leg',(25,34),(28,42),(33,42));self.relate('connect','leg','bird')
