"""Soap Bar with Bubbles.

Plan: Centerline4,8,44,40. Broad cylindrical soap; two open bubbles above. Puddle integrated into the lower silhouette to avoid duplicate close contours.
Construction: No useful direct Lucide match; ellipse top and shared cylinder silhouette.
Reduction: Puddle merged into widened lower outline; two bubbles remain hollow.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa5dde21-7924-4d19-b62c-486697c66c2c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/32-fa5dde21-7924-4d19-b62c-486697c66c2c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'soap-bar-with-bubbles'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('soap', 'bar', 'with', 'bubbles')

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
        path('top',(6,27),[('A',(42,27),18,4,True),('A',(6,27),18,4,True)],True)
        path('body',(6,27),[('L',(6,33)),('L',(4,36)),('C',(12,40),(4,40),(8,40)),('L',(36,40)),('C',(44,36),(40,40),(44,40)),('L',(42,33)),('L',(42,27))])
        circle('bubble-left',15,11,3);circle('bubble-right',34,11,3);join('top','body')
