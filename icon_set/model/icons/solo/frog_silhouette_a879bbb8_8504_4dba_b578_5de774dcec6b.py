"""Frog Amphibian Animal Shape.

Plan: Frog eye humps above squat body and broad splayed hind legs; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Small toes reduced to one front-leg stroke and broad side feet; paired eye lobes retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a879bbb8-8504-4dba-b578-5de774dcec6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/15-a879bbb8-8504-4dba-b578-5de774dcec6b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'frog-silhouette'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('frog', 'silhouette')

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
        path('body',(16,40),[('C',(13,27),(12,36),(11,30)),('C',(10,22),(11,25),(10,24)),('L',(10,15)),('A',(24,15),7,7,True),('A',(38,15),7,7,True),('L',(38,22)),('C',(35,27),(38,24),(37,25)),('C',(32,40),(37,30),(36,36))])
        path('left-leg',(13,27),[('C',(4,30),(6,20),(4,22)),('L',(4,40)),('L',(16,40))]);path('right-leg',(35,27),[('C',(44,30),(42,20),(44,22)),('L',(44,40)),('L',(32,40))]);join('body','left-leg');join('body','right-leg')
        line('front-feet',(24,30),(24,38))
