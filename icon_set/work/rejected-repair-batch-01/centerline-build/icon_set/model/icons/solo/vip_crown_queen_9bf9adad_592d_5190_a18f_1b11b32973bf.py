"""vip-crown-queen: Balanced queen crown; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9bf9adad-592d-5190-a18f-1b11b32973bf'
SOURCE_PATH = 'pictographic-primitives/rewards/vip crown queen_9bf9adad-592d-5190-a18f-1b11b32973bf.svg'
AUTHOR = 'gpt-6'

class VipCrownQueen(Solo48):
    icon_id = 'vip-crown-queen'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('solo-ai-full-set', 'vip-crown-queen')

    def build(self):
        # Plan: Preserve the three-point crown and curved band; mirror the peaks and use matching elliptical band halves.
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
        path('crown',(4,16),[('L',(16,20)),('L',(24,8)),('L',(32,20)),('L',(44,16)),('L',(40,34)),('A',(8,34),16,6,True),('L',(4,16))],True)
        path('band',(8,34),[('A',(40,34),16,6,True)]);join('band','crown')
