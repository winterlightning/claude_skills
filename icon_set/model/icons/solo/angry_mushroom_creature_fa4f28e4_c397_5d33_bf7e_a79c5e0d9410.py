"""Angry Mushroom Creature.

Plan: Mushroom cap with explicit apex and paired angry eyes; two rootlike feet. Extremes4,8,44,40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Small slanted eyes combine eyes and brows; omit mouth to retain clear angry mushroom face.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa4f28e4-c397-5d33-bf7e-a79c5e0d9410'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/30-fa4f28e4-c397-5d33-bf7e-a79c5e0d9410.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'angry-mushroom-creature'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('angry', 'mushroom', 'creature')

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
        path('cap',(4,29),[('C',(24,8),(4,15),(14,8)),('C',(44,29),(34,8),(44,15)),('L',(4,29))],True)
        path('body',(14,29),[('L',(10,40)),('L',(18,40))]);join('cap','body')
        path('body-right',(34,29),[('L',(38,40)),('L',(30,40))]);join('cap','body-right')
        for s in (-1,1):line(f'eye-{s}',(24+s*5,18),(24+s*4,19))
