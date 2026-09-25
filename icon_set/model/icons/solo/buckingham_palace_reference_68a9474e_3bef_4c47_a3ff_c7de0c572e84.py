"""Buckingham Palace Landmark.

Plan: Three towers each8 wide with two8-wide gaps, x4..44 y8..40; notched sides and central pointed spire.
Construction: Lucide castle: readable tower silhouette.
Reduction: Omitted small windows; wider horizontal keyshape fits three distinct towers.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68a9474e-3bef-4c47-a3ff-c7de0c572e84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/15-68a9474e-3bef-4c47-a3ff-c7de0c572e84.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'buckingham-palace-reference'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('buckingham', 'palace', 'reference')

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
        poly('outer',(4,40),(4,20),(8,24),(12,20),(12,32),(20,32),(20,18),(24,8),(28,18),(28,32),(36,32),(36,20),(40,24),(44,20),(44,40),(4,40))
