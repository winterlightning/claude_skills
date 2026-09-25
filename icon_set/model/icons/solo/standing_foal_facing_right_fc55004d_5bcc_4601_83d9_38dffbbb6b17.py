"""Standing Young Horse.

Plan: Right-facing foal with tall neck, pointed ear, rounded muzzle and hanging tail; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Two legs and tail retained; tiny eye and hoof seams omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc55004d-5bcc-4601-83d9-38dffbbb6b17'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/27-fc55004d-5bcc-4601-83d9-38dffbbb6b17.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'standing-foal-facing-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('standing', 'foal', 'facing', 'right')

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
        path('foal',(10,42),[('L',(10,26)),('A',(18,18),8,8,True),('L',(26,18)),('C',(32,8),(26,12),(29,10)),('L',(34,6)),('L',(34,12)),('C',(42,20),(38,15),(42,17)),('L',(42,29)),('L',(34,27)),('L',(34,42)),('L',(26,42)),('L',(26,32)),('L',(18,32)),('L',(18,42)),('L',(10,42))],True)
        path('tail',(10,26),[('C',(6,36),(6,27),(6,31))]);join('foal','tail')
