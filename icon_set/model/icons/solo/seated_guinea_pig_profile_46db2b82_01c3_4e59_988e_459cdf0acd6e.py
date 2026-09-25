"""Small Guinea Pig Pet Animal.

Plan: Guinea pig with rounded back, right-facing muzzle, small ear and two feet; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Tiny mouth and toe lines omitted; round haunch, short muzzle and small ear retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46db2b82-01c3-4e59-988e-459cdf0acd6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/19-46db2b82-01c3-4e59-988e-459cdf0acd6e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'seated-guinea-pig-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('seated', 'guinea', 'pig', 'profile')

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
        path('body',(16,40),[('C',(4,27),(8,40),(4,35)),('C',(21,12),(4,16),(13,12)),('L',(27,12)),('A',(35,12),4,4,True),('C',(44,24),(41,12),(44,18)),('C',(36,31),(44,29),(40,31)),('L',(39,40)),('L',(28,40)),('L',(25,31)),('L',(14,31)),('C',(16,40),(16,33),(16,38))],True)
        self.add_dot('eye',(34,23))
