"""Stylized Pig Face.

Plan: Blank pear-shaped pig head with two broad pointed ears; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Ear partitions integrated into the outer silhouette; no facial marks added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c6e94ae-cd71-4b5c-a6e2-8bcbeb0fce21'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/46-3c6e94ae-cd71-4b5c-a6e2-8bcbeb0fce21.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'blank-pig-head-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('blank', 'pig', 'head', 'outline')

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
        path('pig',(6,6),[('C',(16,13),(10,6),(14,10)),('C',(32,13),(21,10),(27,10)),('C',(42,6),(34,10),(38,6)),('L',(42,16)),('C',(39,23),(42,19),(40,21)),('C',(24,42),(44,38),(36,42)),('C',(9,23),(12,42),(4,38)),('C',(6,16),(8,21),(6,19)),('L',(6,6))],True)
