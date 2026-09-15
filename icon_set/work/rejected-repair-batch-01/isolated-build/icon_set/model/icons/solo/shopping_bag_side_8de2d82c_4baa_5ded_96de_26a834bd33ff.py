"""shopping-bag-side: Regular side-gusset bag; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8de2d82c-4baa-5ded-96de-26a834bd33ff'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag side_8de2d82c-4baa-5ded-96de-26a834bd33ff.svg'
AUTHOR = 'gpt-6'

class ShoppingBagSide(Solo48):
    icon_id = 'shopping-bag-side'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('solo-ai-full-set', 'shopping-bag-side')

    def build(self):
        # Plan: Preserve the side panel and arched handle; widen the side panel and use an exact circular handle arch.
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
        path('bag',(8,44),[('L',(10,16)),('L',(14,16)),('L',(26,16)),('L',(28,16)),('L',(36,16)),('L',(40,44)),('L',(28,44)),('L',(8,44))],True)
        path('handle',(14,16),[('L',(14,10)),('A',(20,4),6,6,True),('A',(26,10),6,6,True),('L',(26,16))]);join('handle','bag')
        line('gusset',(28,16),(28,44));join('gusset','bag')
