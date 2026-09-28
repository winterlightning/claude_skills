"""Human Profile with Eye Insight.

Plan: Centerline8,4,40,44. Right-facing head with round crown, projecting nose, open neck and large almond eye.
Construction: Shared human-reference.md inspected for minimal anatomy; isolated profile, so detached head/body spacing is not applicable.
Reduction: Omitted tiny pupil to keep the almond eye open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c300321-ec3d-4d40-b58f-a6b8a1dcd2dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/49-6c300321-ec3d-4d40-b58f-a6b8a1dcd2dc.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'profile-head-almond-eye'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('profile', 'head', 'almond', 'eye')

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
        path('head',(14,44),[('L',(14,33)),('C',(8,20),(14,29),(8,28)),('A',(36,20),14,16,True),('L',(40,27)),('L',(32,27)),('L',(32,34)),('A',(26,40),6,6,True),('L',(26,44))])
        path('eye',(17,20),[('C',(26,20),(20,14),(24,14)),('C',(17,20),(23,25),(20,25))],True)
