"""Stylized Kangaroo with Baby Joey.

Plan: Seated left-facing kangaroo with upright ears, bent forearm, folded hind leg and long tail; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Tiny eye and bent forepaw omitted; folded hind leg silhouette and rising tail retained; inner haunch line omitted. No separate joey is visible in original.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6430919f-654f-425a-b43e-41534d7647dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/44-6430919f-654f-425a-b43e-41534d7647dd.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'seated-kangaroo-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('seated', 'kangaroo', 'profile')

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
        path('kangaroo',(12,21),[('L',(4,18)),('L',(8,12)),('L',(8,8)),('L',(18,8)),('L',(18,16)),('C',(31,28),(28,16),(31,21)),('C',(44,25),(36,31),(42,28)),('C',(28,37),(42,36),(35,37)),('L',(28,40)),('L',(10,40)),('A',(10,32),4,4,True),('L',(18,32)),('C',(12,21),(12,30),(10,26))],True)
