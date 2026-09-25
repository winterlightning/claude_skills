"""Great Gazoo Character Head.

Plan: Helmet dome with round hanging face and two ball antennae. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Antenna tip circles become round stroke ends; retain the oversized helmet and blank rounded face.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99eb35e8-54a5-4035-8332-a69d96a4a1a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/11-99eb35e8-54a5-4035-8332-a69d96a4a1a0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gazoo-helmeted-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('gazoo', 'helmeted', 'head')

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
        path('helmet',(6,28),[('C',(12,15),(6,23),(8,18)),('C',(24,10),(15,12),(19,10)),('C',(36,15),(29,10),(33,12)),('C',(42,28),(40,18),(42,23))])
        path('face',(12,28),[('A',(36,28),12,14,False)]);
        poly('rim',(6,28),(12,28),(36,28),(42,28));join('face','rim');join('helmet','rim')
        for s in (-1,1):
         x=lambda v:24+s*v
         line(f'stalk-{s}',(x(12),15),(x(18),6));join('helmet',f'stalk-{s}')
         self.add_dot(f'tip-{s}',(x(18),6));join(f'stalk-{s}',f'tip-{s}')
