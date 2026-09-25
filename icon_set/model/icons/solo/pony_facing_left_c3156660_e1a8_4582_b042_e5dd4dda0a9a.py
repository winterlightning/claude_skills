"""Pony Facing Left
Plan: Left-facing pony with short ear, broad legs, sloping neck and hanging tail.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3156660-e1a8-4582-b042-e5dd4dda0a9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pony_c3156660-e1a8-4582-b042-e5dd4dda0a9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pony-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pony', 'horse', 'animal', 'tail', 'livestock', 'equine')

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
        path('pony',(4,18),[('L',(11,8)),('L',(16,11)),('C',(22,23),(21,14),(21,20)),('L',(34,23)),('C',(36,28),(36,23),(36,25)),('L',(36,40)),('L',(26,40)),('L',(26,31)),('L',(18,31)),('L',(17,40)),('L',(8,40)),('L',(9,23)),('C',(4,18),(4,26),(4,23))],True)
        path('tail',(34,23),[('C',(44,29),(44,23),(44,26)),('L',(44,36))]);self.relate('connect','tail','pony')
