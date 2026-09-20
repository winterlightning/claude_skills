"""Human Portrait Draft Sketch.

Plan: Circular portrait construction head with crossing guides over rounded shoulders. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Circular face and touching shoulders follow human reference rules; retain both portrait guidelines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd53a710-719c-568e-86b2-b68384d280c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/14-fd53a710-719c-568e-86b2-b68384d280c0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'portrait-construction-sketch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ()
    keywords = ('portrait', 'construction', 'sketch')

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
        path('head',(24,6),[('A',(36,18),12,12,True),('A',(24,30),12,12,True),('A',(12,18),12,12,True),('A',(24,6),12,12,True)],True)
        poly('guide-v',(24,6),(24,18),(24,30));poly('guide-h',(12,18),(24,18),(36,18));join('head','guide-v');join('head','guide-h');join('guide-v','guide-h')
        path('body',(6,42),[('A',(14,34),8,8,True),('L',(34,34)),('A',(42,42),8,8,True)]);join('head','body')
