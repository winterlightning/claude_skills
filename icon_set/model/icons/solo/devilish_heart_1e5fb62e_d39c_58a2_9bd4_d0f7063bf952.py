"""Devilish Heart with Horns and Tail.

Plan: Devil heart with exact shared horn apexes and tail attachment. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Solid horns and open arrow tip avoid small holes. Each attachment has an explicit shared node.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e5fb62e-d39c-58a2-9bd4-d0f7063bf952'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/46-1e5fb62e-d39c-58a2-9bd4-d0f7063bf952.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'devilish-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('devilish', 'heart')

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
        path('heart',(22,18),[('C',(31,14),(25,14),(28,14)),('C',(36,22),(34,14),(36,18)),('C',(30,29),(36,25),(33,27)),('C',(22,34),(27,31),(24,33)),('C',(8,22),(16,31),(8,27)),('C',(13,14),(8,18),(10,14)),('C',(22,18),(16,14),(19,14))],True)
        line('horn-left',(13,14),(6,6));join('heart','horn-left')
        line('horn-right',(31,14),(38,6));join('heart','horn-right')
        path('tail',(30,29),[('L',(36,29)),('A',(42,35),6,6,True),('A',(36,41),6,6,True),('L',(24,41))]);join('heart','tail')
        poly('arrow',(27,38),(24,41),(27,42));join('tail','arrow')
