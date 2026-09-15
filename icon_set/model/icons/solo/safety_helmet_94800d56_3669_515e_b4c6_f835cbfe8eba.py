"""safety-helmet: Smooth hard hat; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94800d56-3669-515e-b4c6-f835cbfe8eba'
SOURCE_PATH = 'icons-json/construction/safety helmet_94800d56-3669-515e-b4c6-f835cbfe8eba.json'
AUTHOR = 'gpt-6'

class SafetyHelmet(Solo48):
    icon_id = 'safety-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('solo-ai-full-set', 'safety-helmet')

    def build(self):
        # Plan: Preserve the tall crown, center reinforcement and broad brim; use matched sides and a clear brim opening.
        # Reference: Lucide hard-hat: original and atomic-debug geometry.

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
        path('crown',(7,31),[('L',(7,25)),('C',(19,8),(7,17),(13,9)),('L',(29,8)),('C',(41,25),(35,9),(41,17)),('L',(41,31))])
        path('brim',(7,31),[('L',(41,31)),('C',(44,35),(44,31),(44,32)),('C',(40,40),(44,39),(43,40)),('L',(8,40)),('C',(4,35),(5,40),(4,39)),('C',(7,31),(4,32),(4,31))],True);join('crown','brim')
        path('ridge',(19,8),[('L',(19,22)),('L',(29,22)),('L',(29,8))]);join('ridge','crown')
