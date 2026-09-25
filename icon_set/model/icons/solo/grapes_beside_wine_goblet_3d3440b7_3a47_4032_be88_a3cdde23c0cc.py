"""Grape Bunch and Wine Glass.

Plan: Three round grapes in a triangular bunch beside a wine glass; radius3 grapes, bounds (6,6)-(42,42).
Construction: Lucide wine: rounded bowl and centered stem/foot; grape circles share radius.
Reduction: Seven overlapping grapes reduced to three separated grapes in one triangular bunch; leaf stem omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d3440b7-3a47-4032-be88-a3cdde23c0cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/37-3d3440b7-3a47-4032-be88-a3cdde23c0cc.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'grapes-beside-wine-goblet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('grapes', 'beside', 'wine', 'goblet')

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
        for j,(x,y) in enumerate(((9,9),(23,9),(16,22))):circle(f'grape-{j}',x,y,3)
        path('bowl',(28,24),[('L',(42,24)),('L',(42,27)),('A',(35,34),7,7,True),('A',(28,27),7,7,True),('L',(28,24))],True)
        line('stem',(35,34),(35,42));poly('foot',(28,42),(35,42),(42,42));join('bowl','stem');join('stem','foot')
