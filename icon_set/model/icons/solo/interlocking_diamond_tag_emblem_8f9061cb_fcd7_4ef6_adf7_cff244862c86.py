"""Google Tag Manager Symbol.

Plan: Geometric interlocking Tag Manager diamond; symmetric outer square and central diamond opening; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Two interlocking bands preserved; square corners replace the tiny outer corner rounding.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f9061cb-fcd7-4ef6-adf7-cff244862c86'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/35-8f9061cb-fcd7-4ef6-adf7-cff244862c86.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'interlocking-diamond-tag-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('interlocking', 'diamond', 'tag', 'emblem')

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
        poly('outer',(24,6),(42,24),(24,42),(6,24),closed=True)
        poly('opening',(24,18),(30,24),(24,30),(18,24),closed=True)
        line('seam-upper',(33,15),(24,18));line('seam-lower',(15,33),(24,30))
        join('outer','seam-upper');join('outer','seam-lower');join('opening','seam-upper');join('opening','seam-lower')
