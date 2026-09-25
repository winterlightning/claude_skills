"""Snail with Spiral Shell.

Plan: Snail with single coherent shell spiral, low foot and paired feelers; bounds (4,8)-(44,40).
Construction: Lucide snail: progressing spiral arcs plus low foot and two upward feelers.
Reduction: Spiral reduced to one broad turn, preserving inward curl and complete snail body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ee72559-60e2-412c-9898-e4dd5004eac8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/48-9ee72559-60e2-412c-9898-e4dd5004eac8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'snail-with-spiral-shell'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('snail', 'with', 'spiral', 'shell')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('shell',(4,20),[('A',(28,20),12,12,True),('A',(12,20),8,8,True),('A',(20,20),4,4,True)])
        path('body',(4,20),[('C',(4,40),(4,31),(14,35)),('L',(32,40)),('L',(36,40)),('A',(44,32),8,8,False),('L',(44,22)),('A',(40,18),4,4,False),('A',(36,22),4,4,False),('L',(36,30))]);join('shell','body')
        line('feeler-left',(36,22),(36,12));line('feeler-right',(44,22),(44,8));join('body','feeler-left');join('body','feeler-right')
