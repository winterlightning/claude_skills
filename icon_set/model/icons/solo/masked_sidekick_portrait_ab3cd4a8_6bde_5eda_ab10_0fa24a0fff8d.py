"""Masked Superhero Sidekick Avatar.

Plan: Sidekick circular face with eye band, swept hair and touching shoulders. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Use a broad plain mask band; reduce swept hair to one angled projecting tuft. Keep the circular face and touching rounded shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab3cd4a8-6bde-5eda-ab10-0fa24a0fff8d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/23-ab3cd4a8-6bde-5eda-ab10-0fa24a0fff8d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'masked-sidekick-portrait'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('masked', 'sidekick', 'portrait')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = "shoulder-top" if name == "body" and index == 1 else f"{name}-{index}"
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
        path('head',(12,14),[('A',(36,14),13,13,True),('A',(36,24),13,13,True),('A',(12,24),13,13,True),('A',(12,14),13,13,True)],True)
        line('mask-top',(12,14),(36,14));line('mask-bottom',(12,24),(36,24));join('head','mask-top');join('head','mask-bottom')
        poly('hair',(12,14),(6,6));join('head','hair');join('mask-top','hair')
        path('body',(6,42),[('A',(14,36),8,6,True),('L',(34,36)),('A',(42,42),8,6,True)]);join('head','body')
