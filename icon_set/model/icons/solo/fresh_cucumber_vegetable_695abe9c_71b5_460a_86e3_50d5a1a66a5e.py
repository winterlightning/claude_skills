"""Fresh Cucumber Vegetable.

Plan: Broad diagonal cucumber capsule with one center mark and short stem, bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Three skin marks reduced to one; widened body for clear space around the central skin mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '695abe9c-71b5-460a-86e3-50d5a1a66a5e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/12-695abe9c-71b5-460a-86e3-50d5a1a66a5e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fresh-cucumber-vegetable'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fresh', 'cucumber', 'vegetable')

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
        path('cucumber',(6,32),[('C',(10,23),(6,28),(8,25)),('L',(23,10)),('C',(32,6),(25,8),(28,6)),('C',(42,16),(38,6),(42,10)),('C',(38,25),(42,20),(40,23)),('L',(25,38)),('C',(16,42),(23,40),(20,42)),('C',(6,32),(10,42),(6,38))],True)
        line('mark',(21,27),(27,21))
        line('stem',(39,9),(42,6));join('cucumber','stem')
