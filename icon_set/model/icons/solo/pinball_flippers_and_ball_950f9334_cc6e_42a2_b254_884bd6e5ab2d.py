"""Pinball Flippers and Ball.

Plan: Two rounded inward flippers and separate pinball. Extremes4,8,44,40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Broaden flippers to preserve both outlined paddles and central ball.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '950f9334-cc6e-42a2-b254-884bd6e5ab2d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/31-950f9334-cc6e-42a2-b254-884bd6e5ab2d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pinball-flippers-and-ball'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('pinball', 'flippers', 'and', 'ball')

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
        circle('ball',24,15,7)
        path('left',(4,32),[('A',(10,26),6,6,True),('L',(19,33)),('L',(18,40)),('L',(4,40)),('L',(4,32))],True)
        path('right',(44,32),[('A',(38,26),6,6,False),('L',(29,33)),('L',(30,40)),('L',(44,40)),('L',(44,32))],True)
