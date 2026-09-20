"""Gymnastics Rings and Balance Beam.

Plan: Two hanging rings above a beam with splayed legs; repeated radius4, bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Short feet and long leg projection reduced to two splayed supports; both rings retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '870ca593-c5d2-40d3-ab70-7e11ade9655b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/47-870ca593-c5d2-40d3-ab70-7e11ade9655b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gymnastics-rings-above-balance-beam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('gymnastics', 'rings', 'above', 'balance', 'beam')

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
        for j,x in enumerate((14,34)):
         path(f'ring-{j}',(x,14),[('A',(x,22),4,4,True),('A',(x,14),4,4,True)],True)
         line(f'strap-{j}',(x,6),(x,14));join(f'ring-{j}',f'strap-{j}')
        poly('beam',(6,31),(14,31),(34,31),(42,31),(42,39),(6,39),closed=True)
        line('left-leg',(14,39),(10,42));line('right-leg',(34,39),(38,42));join('beam','left-leg');join('beam','right-leg')
