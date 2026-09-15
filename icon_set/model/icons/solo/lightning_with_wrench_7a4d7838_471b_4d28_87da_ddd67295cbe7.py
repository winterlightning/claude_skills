"""lightning-with-wrench: Clear wrench and lightning; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a4d7838-471b-4d28-87da-ddd67295cbe7'
SOURCE_PATH = 'icons-json/symbol/lightning with wrench_7a4d7838-471b-4d28-87da-ddd67295cbe7.json'
AUTHOR = 'gpt-6'

class LightningWithWrench(Solo48):
    icon_id = 'lightning-with-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'lightning-with-wrench')

    def build(self):
        # Plan: Preserve a diagonal wrench and separate bolt. Rebalance the two symbols with a wider open wrench handle.
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
        path('wrench',(6,32),[('L',(17,19)),('C',(15,13),(15,18),(14,16)),('C',(24,6),(15,8),(20,6)),('L',(31,6)),('L',(24,12)),('L',(27,17)),('C',(22,25),(28,22),(26,25)),('L',(14,38))])
        poly('bolt',(42,22),(29,32),(42,32),(32,42))
