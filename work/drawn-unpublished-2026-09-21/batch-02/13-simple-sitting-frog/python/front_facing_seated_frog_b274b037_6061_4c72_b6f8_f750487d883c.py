"""Front-Facing Seated Frog
Plan: Eye bulges, upright belly and paired folded hind legs.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Foreleg lines omitted to preserve belly opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b274b037-6061-4c72-b6f8-f750487d883c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amphibian frog body_b274b037-6061-4c72-b6f8-f750487d883c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-seated-frog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('frog', 'amphibian', 'seated', 'legs', 'animal', 'pond', 'wildlife')

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
        path('frog',(12,20),[('C',(12,11),(9,17),(10,13)),('A',(24,11),6,5,True),('A',(36,11),6,5,True),('C',(36,20),(38,13),(39,17)),('C',(34,27),(35,22),(34,24)),('C',(24,42),(38,37),(33,42)),('C',(14,27),(15,42),(10,37)),('C',(12,20),(14,24),(13,22))],True)
        path('left-haunch',(14,29),[('C',(6,28),(8,21),(6,24)),('C',(10,39),(6,33),(8,36)),('L',(6,42))])
        path('right-haunch',(34,29),[('C',(42,28),(40,21),(42,24)),('C',(38,39),(42,33),(40,36)),('L',(42,42))])
        self.relate('connect','frog','left-haunch');self.relate('connect','frog','right-haunch')
