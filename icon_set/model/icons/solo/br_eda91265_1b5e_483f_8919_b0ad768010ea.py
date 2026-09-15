"""br: Regular Br lettering; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eda91265-1b5e-483f-8919-b0ad768010ea'
SOURCE_PATH = 'icons-json/symbol/Br_eda91265-1b5e-483f-8919-b0ad768010ea.json'
AUTHOR = 'gpt-6'

class Br(Solo48):
    icon_id = 'br'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'br')

    def build(self):
        # Plan: Preserve the capital B and lowercase r; use broad rounded bowls and an explicitly joined shoulder.
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
        path('upper-b',(4,24),[('L',(4,8)),('L',(12,8)),('C',(20,16),(18,8),(20,11)),('C',(12,24),(20,21),(18,24)),('L',(4,24))],True)
        path('lower-b',(4,24),[('L',(4,40)),('L',(12,40)),('C',(22,32),(18,40),(22,37)),('C',(12,24),(22,27),(18,24))]);join('lower-b','upper-b')
        path('r-stem',(32,18),[('L',(32,22)),('L',(32,40))]);path('r-shoulder',(32,22),[('C',(44,20),(35,16),(42,16))]);join('r-stem','r-shoulder')
