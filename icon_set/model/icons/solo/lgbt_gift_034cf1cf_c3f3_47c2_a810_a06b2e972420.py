"""lgbt-gift: Balanced gift bow; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '034cf1cf-c3f3-47c2-a810-a06b2e972420'
SOURCE_PATH = 'icons-json/symbol/lgbt gift_034cf1cf-c3f3-47c2-a810-a06b2e972420.json'
AUTHOR = 'gpt-6'

class LgbtGift(Solo48):
    icon_id = 'lgbt-gift'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'lgbt-gift')

    def build(self):
        # Plan: Two mirrored bow loops retain the wrapped-gift silhouette and meet the box at its center.
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
        path('box',(8,18),[('L',(24,18)),('L',(40,18)),('L',(40,44)),('L',(8,44)),('L',(8,18))],True)
        for j,mirror in enumerate([False,True]):
         def p(x,y):return (48-x,y) if mirror else (x,y)
         path(f'bow-{j}',p(24,18),[('C',p(12,4),p(22,10),p(16,4)),('C',p(8,8),p(9,4),p(8,5)),('C',p(24,18),p(8,15),p(16,18))],True);join(f'bow-{j}','box')
        join('bow-0','bow-1')
