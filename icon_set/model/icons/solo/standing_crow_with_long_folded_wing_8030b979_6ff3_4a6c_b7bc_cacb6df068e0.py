"""Standing Crow with Long Folded Wing
Plan: Right-facing crow with angular long tail, beak and one visible bent leg.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bird: continuous breast and long tail.
Reduction: Small eye and interior wing seam omitted for clear negative space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8030b979-6ff3-4a6c-b7bc-cacb6df068e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crow_8030b979-6ff3-4a6c-b7bc-cacb6df068e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-crow-with-long-folded-wing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crow', 'bird', 'wing', 'tail', 'beak', 'wildlife', 'perched')

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
        path('crow',(6,38),[('L',(25,15)),('C',(34,6),(27,9),(28,6)),('L',(42,11)),('L',(36,14)),('C',(27,33),(36,27),(33,31)),('L',(14,36)),('L',(6,38))],True)
        self.add_polyline('leg',(27,33),(31,42),(38,42));self.relate('connect','leg','crow')
