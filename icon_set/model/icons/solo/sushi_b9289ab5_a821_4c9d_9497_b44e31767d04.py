"""sushi: Balanced striped sushi; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b9289ab5-a821-4c9d-9497-b44e31767d04'
SOURCE_PATH = 'pictographic-primitives/food/sushi_b9289ab5-a821-4c9d-9497-b44e31767d04.svg'
AUTHOR = 'gpt-6'

class Sushi(Solo48):
    icon_id = 'sushi'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('solo-ai-full-set', 'sushi')

    def build(self):
        # Plan: Preserve the oval rice and arched striped topping. Use a single shared top edge instead of overlapping rice and topping contours.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        path('rice',(8,26),[('C',(24,22),(12,22),(17,22)),('C',(40,26),(31,22),(36,22)),('C',(32,40),(43,34),(39,40)),('L',(16,40)),('C',(8,26),(9,40),(5,34))],True)
        path('top',(8,26),[('L',(4,25)),('C',(13,12),(6,17),(8,14)),('C',(24,8),(17,9),(20,8)),('C',(35,12),(28,8),(31,9)),('C',(44,25),(40,14),(42,17)),('L',(40,26))]);join('top','rice')
        line('stripe-mid',(24,8),(24,22));join('stripe-mid','top');join('stripe-mid','rice')
