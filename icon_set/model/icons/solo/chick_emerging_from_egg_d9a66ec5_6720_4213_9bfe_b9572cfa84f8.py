"""Chick Hatching from Egg.

Plan: Round-headed chick over broad jagged eggshell, right-pointing bill stroke; x6..42 y6..42.
Construction: Lucide egg: broad shell and coherent hatchling silhouette.
Reduction: Reduced tiny triangular beak to projecting bill stroke, omitted eye and widened shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9a66ec5-6720-4213-9bfe-b9572cfa84f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/35-d9a66ec5-6720-4213-9bfe-b9572cfa84f8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'chick-emerging-from-egg'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('chick', 'emerging', 'from', 'egg')

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
        path('shell',(6,26),[('L',(14,32)),('L',(24,26)),('L',(34,32)),('L',(42,26)),('A',(6,26),18,16,True)],True)
        path('chick',(6,26),[('C',(14,18),(8,22),(10,20)),('L',(14,16)),('A',(34,16),10,10,True),('C',(42,26),(34,22),(38,24))]);join('chick','shell')
        line('bill',(34,16),(42,16));join('bill','chick')
