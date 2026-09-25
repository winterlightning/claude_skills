"""Classic Manual Typewriter.

Plan: Blank sheet, rounded carriage with side knobs, broad tapered base;6..42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Knobs reduced to round-ended short strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6f6d350-b6a8-45da-bd97-1b1c2f4110c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/46-e6f6d350-b6a8-45da-bd97-1b1c2f4110c6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'compact-typewriter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('compact', 'typewriter')

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
        path('paper',(14,18),[('L',(14,10)),('A',(18,6),4,4,True),('L',(30,6)),('A',(34,10),4,4,True),('L',(34,18))])
        rect('carriage',10,18,28,8,4);join('paper','carriage')
        path('base',(14,26),[('L',(6,36)),('A',(12,42),6,6,False),('L',(36,42)),('A',(42,36),6,6,False),('L',(34,26))]);join('base','carriage')
        line('knob-left',(6,22),(10,22));line('knob-right',(38,22),(42,22));join('knob-left','carriage');join('knob-right','carriage')
