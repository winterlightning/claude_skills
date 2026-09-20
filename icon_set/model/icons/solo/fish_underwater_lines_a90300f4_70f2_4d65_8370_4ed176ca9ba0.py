"""Fish Swimming Underwater.

Plan: Centerline4,8,44,40. Right-facing fish with open forked tail under three horizontal water strokes.
Construction: Lucide fish original/debug: pointed snout, curved body and forked tail.
Reduction: Fin notches and tiny eye omitted; third water stroke shortened and tail reduced to an open fork.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a90300f4-70f2-4d65-8370-4ed176ca9ba0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/16-a90300f4-70f2-4d65-8370-4ed176ca9ba0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fish-underwater-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fish', 'underwater', 'lines')

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
        for y,w in ((8,44),(16,44),(24,12)):line(f'water-{y}',(4,y),(w,y))
        path('fish',(14,35),[('C',(30,30),(20,30),(24,30)),('C',(44,35),(36,30),(40,32)),('C',(30,40),(40,38),(36,40)),('C',(14,35),(24,40),(20,40))],True)
        poly('tail',(4,33),(14,35),(4,40));join('tail','fish')
