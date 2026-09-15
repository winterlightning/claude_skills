"""award-medal-rewards: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '319fc61d-077f-5c65-942b-278d5d4da881'
SOURCE_PATH = 'icons-json/rewards/award medal_319fc61d-077f-5c65-942b-278d5d4da881.json'
AUTHOR = 'gpt-6'

class AwardMedalRewards(Solo48):
    icon_id = 'award-medal-rewards'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('award', 'medal', 'rewards', 'solo-ai-first50')

    def build(self):
        # Plan: A broad symmetric ribbon connects at two exact 3-4-5 points on a circular medal. Removed the cramped ribbon stripe and used one true medal radius.
        # Reference: Lucide original/medal.svg and atomic-debug/medal.svg.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
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
        path('medal',(16,28), [('A',(32,28),10,10,True),('A',(34,34),10,10,True),('A',(14,34),10,10,True),('A',(16,28),10,10,True)],True)
        poly('ribbon',(16,28),(8,4),(40,4),(32,28));join('medal','ribbon')

