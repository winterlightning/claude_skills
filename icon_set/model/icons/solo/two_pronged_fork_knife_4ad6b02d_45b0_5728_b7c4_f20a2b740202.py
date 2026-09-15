"""two-pronged-fork-knife: Clean fork and knife; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ad6b02d-45b0-5728-b7c4-f20a2b740202'
SOURCE_PATH = 'icons-json/food/two pronged fork knife_4ad6b02d-45b0-5728-b7c4-f20a2b740202.json'
AUTHOR = 'gpt-6'

class TwoProngedForkKnife(Solo48):
    icon_id = 'two-pronged-fork-knife'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('solo-ai-full-set', 'two-pronged-fork-knife')

    def build(self):
        # Plan: Preserve the two utensils; split the knife blade and handle at their real join and center the fork stem.
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
        path('blade',(8,4),[('C',(16,25),(14,9),(16,18)),('L',(8,25)),('L',(8,4))],True)
        line('knife-handle',(8,25),(8,44));join('knife-handle','blade')
        path('fork',(28,4),[('L',(28,14)),('A',(34,20),6,6,False),('A',(40,14),6,6,False),('L',(40,4))]);line('fork-handle',(34,20),(34,44));join('fork-handle','fork')
