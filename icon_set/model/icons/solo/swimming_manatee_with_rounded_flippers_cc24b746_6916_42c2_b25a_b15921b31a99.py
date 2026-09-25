"""Swimming Manatee with Rounded Flippers
Plan: Swimming manatee with paddle tail, drooping flipper and rounded muzzle.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Tiny eye omitted; flipper retained as an open internal curve."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc24b746-6916-42c2-b25a-b15921b31a99'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/manatee_cc24b746-6916-42c2-b25a-b15921b31a99.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'swimming-manatee-with-rounded-flippers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('manatee', 'animal', 'marine', 'flipper', 'tail', 'swimming', 'mammal')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('manatee',(4,35),[('C',(9,25),(4,28),(6,25)),('C',(27,8),(9,12),(21,8)),('C',(44,20),(37,8),(44,14)),('C',(35,24),(44,29),(38,29)),('C',(25,31),(36,32),(31,32)),('L',(18,32)),('L',(12,40)),('L',(8,37)),('L',(4,40)),('L',(4,35))],True)
        path('flipper',(27,22),[('C',(25,31),(23,26),(22,31))]);join('flipper','manatee')
