"""t-shirt-clothes: Balanced short sleeves; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b53f582-4552-4079-9580-b9a0440eed2e'
SOURCE_PATH = 'icons-json/clothes/t shirt_3b53f582-4552-4079-9580-b9a0440eed2e.json'
AUTHOR = 'gpt-6'

class TShirtClothes(Solo48):
    icon_id = 't-shirt-clothes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('solo-ai-full-set', 't-shirt-clothes')

    def build(self):
        # Plan: Matching short sleeves with horizontal cuffs, a shallow round neck and a straight body.
        # Reference: Lucide shirt: original and atomic-debug geometry.

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
        path('shirt',(17,8),[('C',(31,8),(21,12),(27,12)),('L',(44,14)),('L',(40,22)),('L',(32,22)),('L',(32,40)),('L',(16,40)),('L',(16,22)),('L',(8,22)),('L',(4,14)),('L',(17,8))],True)
