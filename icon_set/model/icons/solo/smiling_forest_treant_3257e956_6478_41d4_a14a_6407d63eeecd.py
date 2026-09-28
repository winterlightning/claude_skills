"""Cute Smiling Forest Treant.

Plan: Treant: scalloped canopy, broad trunk, horizontal branch arms and two roots. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Branch arms become solid short strokes; shallow split feet and three canopy lobes remain.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3257e956-6478-41d4-a14a-6407d63eeecd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/44-3257e956-6478-41d4-a14a-6407d63eeecd.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'smiling-forest-treant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('smiling', 'forest', 'treant')

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
        path('tree',(11,18),[('C',(6,12),(6,18),(6,15)),('A',(12,6),6,6,True),('C',(24,6),(16,6),(20,10)),('C',(36,6),(28,10),(32,6)),('A',(42,12),6,6,True),('C',(37,18),(42,15),(42,18)),('L',(37,28)),('L',(37,32)),('L',(37,42)),('L',(28,42)),('L',(28,38)),('L',(20,38)),('L',(20,42)),('L',(11,42)),('L',(11,32)),('L',(11,28)),('L',(11,18))],True)
        for x,end in [(11,6),(37,42)]:line(f'arm-{x}',(x,28),(end,28));join('tree',f'arm-{x}')
        for x in (20,28):self.add_dot(f'eye-{x}',(x,18))
        poly('smile',(20,27),(24,29),(28,27))
