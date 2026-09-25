"""Horned Viking Helmet.

Plan: Viking helmet with central ridge, long face and upward horns. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Helmet band and horns become single strokes; preserve central ridge and long blank face.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b165e949-7c1a-5f3a-9cc9-d872f054a0b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/13-b165e949-7c1a-5f3a-9cc9-d872f054a0b2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'horned-viking-portrait'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('horned', 'viking', 'portrait')

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
        path('dome',(12,20),[('A',(24,8),12,12,True),('A',(36,20),12,12,True)])
        poly('band',(10,20),(12,20),(24,20),(36,20),(38,20));join('dome','band')
        line('ridge',(24,8),(24,20));join('dome','ridge');join('band','ridge')
        path('face',(12,20),[('L',(12,30)),('A',(24,42),12,12,False),('A',(36,30),12,12,False),('L',(36,20))]);join('face','band')
        for s in (-1,1):
         x=lambda v:24+s*v
         path(f'horn-{s}',(x(12),20),[('C',(x(18),6),(x(18),20),(x(18),12))]);join('dome',f'horn-{s}');join('band',f'horn-{s}');join('face',f'horn-{s}')
