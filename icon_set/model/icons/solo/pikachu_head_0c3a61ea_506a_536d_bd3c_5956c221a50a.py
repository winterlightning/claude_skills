"""Pikachu Head Icon.

Plan: Long-eared yellow mouse bust with round face and short shoulder strokes. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Long ears become solid strokes; small mouth and ear interiors omitted. Retain round head, paired eyes and shoulder hints.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c3a61ea-506a-536d-bd3c-5956c221a50a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/30-0c3a61ea-506a-536d-bd3c-5956c221a50a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pikachu-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('pikachu', 'head')

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
        path('head',(12,22),[('A',(24,14),13,13,True),('A',(36,22),13,13,True),('A',(36,32),13,13,True),('A',(24,40),13,13,True),('A',(12,32),13,13,True),('A',(12,22),13,13,True)],True)
        line('ear-left',(12,22),(6,6));line('ear-right',(36,22),(42,6));join('head','ear-left');join('head','ear-right')
        for x in (20,28):self.add_dot(f'eye-{x}',(x,25))
        line('shoulder-left',(12,32),(6,42));line('shoulder-right',(36,32),(42,42));join('head','shoulder-left');join('head','shoulder-right')
