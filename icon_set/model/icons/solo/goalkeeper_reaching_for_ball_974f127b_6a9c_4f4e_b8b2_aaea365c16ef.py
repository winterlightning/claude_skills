"""Goalkeeper Catching Ball.

Plan: Goalkeeper reaching to ball, horizontal shoulders, exact aligned head/torso gap8; bounds (6,6)-(42,42).
Construction: Shared human full_body_ref.png: circle head and stroke limbs, head radius4 y10; torso neck16,22 gives exact4 ink gap.
Reduction: Source partial lower body completed as two legs; reaching action retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '974f127b-6a9c-4f4e-b8b2-aaea365c16ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/33-974f127b-6a9c-4f4e-b8b2-aaea365c16ef.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'goalkeeper-reaching-for-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('goalkeeper', 'reaching', 'for', 'ball')

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
        circle('head',16,10,4)
        line('torso',(16,22),(16,32));self.mark_human_figure('keeper',head='head',torso='torso',torso_junction='start')
        poly('arms',(6,32),(6,22),(16,22),(28,22),(36,20));join('torso','arms')
        poly('legs',(8,42),(16,32),(25,42));join('torso','legs')
        path('ball',(36,20),[('A',(36,8),6,6,True),('A',(36,20),6,6,True)],True);join('arms','ball')
