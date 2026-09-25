"""Bird Nest with Egg.

Plan: Egg behind a left-facing bird whose lower contour forms the nest bowl; deliberate asymmetric head at right.
Construction: Lucide egg: broad smooth egg silhouette.
Reduction: Omitted tiny facial detail absent from original; kept bird, egg and bowl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24877473-aa74-4eb9-a2ef-3b61dec1c3f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/02-24877473-aa74-4eb9-a2ef-3b61dec1c3f5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bird-egg-nest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('bird', 'egg', 'nest')

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
        path('bird',(4,25),[('C',(14,25),(8,22),(10,24)),('C',(28,29),(18,27),(24,30)),('L',(28,20)),('L',(23,17)),('C',(31,14),(24,15),(26,14)),('C',(35,13),(32,13),(34,13)),('C',(44,24),(41,13),(44,18)),('C',(24,40),(44,34),(36,40)),('C',(4,25),(12,40),(4,34))],True)
        path('egg',(14,25),[('C',(18,8),(12,17),(12,8)),('C',(23,17),(23,8),(23,12))]);join('egg','bird')
