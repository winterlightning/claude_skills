"""Bottle Conveyor Belt Production Line.

Plan: Three bottle bodies at 16-unit pitch, each 8 wide, over an 8-high capsule belt; extremes x4..44 y8..40.
Construction: Lucide library repeat spacing; book-like repeated upright silhouettes.
Reduction: Removed four belt chevrons; simplified bottle necks to short stems because outlined neck walls cannot fit.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e5180cb-0141-4efb-92ff-76a1f26e5081'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/07-2e5180cb-0141-4efb-92ff-76a1f26e5081.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-bottles-on-conveyor-belt'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('three', 'bottles', 'on', 'conveyor', 'belt')

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
        for j,x in enumerate((4,20,36)):
         rect(f'bottle-{j}',x,12,8,12,2)
         line(f'neck-{j}',(x+4,8),(x+4,12));join(f'neck-{j}',f'bottle-{j}')
        rect('belt',4,32,40,8,4)
