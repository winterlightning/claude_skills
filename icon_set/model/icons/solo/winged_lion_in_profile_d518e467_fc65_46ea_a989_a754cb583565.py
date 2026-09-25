"""Mythical Winged Lion.

Plan: Winged lion right-facing, feathered raised wing, mane and four-legged body. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Retain the four-legged animal silhouette, raised broad wing, rounded head and short curled tail. Omit the eye, mane scallops and distant legs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd518e467-fc65-46ea-a989-a754cb583565'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/27-d518e467-fc65-46ea-a989-a754cb583565.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'winged-lion-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('winged', 'lion', 'in', 'profile')

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
        path('lion',(6,42),[('L',(6,33)),('C',(12,27),(6,29),(9,27)),('L',(16,27)),('L',(7,6)),('L',(24,10)),('L',(24,25)),('L',(32,25)),('L',(32,19)),('A',(38,13),6,6,True),('C',(42,19),(42,13),(42,16)),('C',(36,29),(42,25),(41,29)),('L',(36,34)),('L',(42,42)),('L',(32,42)),('L',(26,35)),('L',(15,35)),('L',(15,42)),('L',(6,42))],True)
        path('tail',(6,33),[('C',(8,22),(6,28),(6,22))]);join('lion','tail')
