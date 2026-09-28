"""Kraken Silhouette
Plan: Open symmetric dome with two curled tentacle tips.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Only the two source tentacles; no invented facial details."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '692731e6-c96e-4519-9f33-286ad47aea95'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kraken_692731e6-c96e-4519-9f33-286ad47aea95.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kraken-silhouette-reference-692731e6'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('kraken', 'sea', 'monster', 'tentacles', 'creature', 'octopus', 'outline')

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
        path('kraken',(4,30),[('C',(9,40),(10,29),(4,40)),('C',(14,30),(15,40),(16,35)),('C',(24,8),(14,18),(16,8)),('C',(34,30),(32,8),(34,18)),('C',(39,40),(32,35),(33,40)),('C',(44,30),(44,40),(38,29))])
