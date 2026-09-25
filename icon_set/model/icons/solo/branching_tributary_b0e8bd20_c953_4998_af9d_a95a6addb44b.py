"""Branching River Tributaries.

Plan: Asymmetric river banks x8..40, y4..44; shared branching node near left center.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Retained all three branch openings; irregular bank directions are intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0e8bd20-c953-4998-af9d-a95a6addb44b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/10-b0e8bd20-c953-4998-af9d-a95a6addb44b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'branching-tributary'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('branching', 'tributary')

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
        path('left-bank',(16,44),[('L',(16,30)),('C',(16,22),(16,27),(16,25)),('C',(8,4),(16,14),(8,14))])
        path('upper-fork',(16,22),[('C',(32,4),(22,13),(32,17))]);join('left-bank','upper-fork')
        path('right-bank',(25,44),[('L',(25,33)),('C',(40,19),(25,26),(35,23))])
