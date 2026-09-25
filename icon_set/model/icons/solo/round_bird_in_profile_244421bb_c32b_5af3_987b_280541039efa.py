"""Simple Round Bird Profile.

Plan: Round bird with projecting left beak and two solid tail feathers. Extremes4,8,44,40.
Construction: Lucide bird original/atomic-debug: clear beak/body boundary and sparse eye.
Reduction: Tail feathers become two solid strokes; omit the detached tiny dash below the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '244421bb-c32b-5af3-987b-280541039efa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/46-244421bb-c32b-5af3-987b-280541039efa.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'round-bird-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('round', 'bird', 'in', 'profile')

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
        path('body',(12,16),[('C',(26,8),(15,10),(21,8)),('C',(36,20),(34,8),(36,13)),('L',(36,24)),('L',(36,32)),('A',(28,40),8,8,True),('L',(20,40)),('A',(12,32),8,8,True),('L',(12,26))])
        path('beak',(4,16),[('L',(12,16)),('C',(18,22),(17,16),(18,18)),('C',(12,26),(18,25),(15,26)),('C',(4,16),(5,26),(4,21))],True);join('body','beak')
        for y in (24,32):line(f'tail-{y}',(36,y),(44,y));join('body',f'tail-{y}')
        self.add_dot('eye',(27,21))
