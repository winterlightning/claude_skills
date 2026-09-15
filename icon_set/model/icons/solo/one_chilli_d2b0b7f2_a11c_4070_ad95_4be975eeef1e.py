"""one-chilli: Smooth curved chilli; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd2b0b7f2-a11c-4070-ad95-4be975eeef1e'
SOURCE_PATH = 'pictographic-primitives/symbol/one chilli_d2b0b7f2-a11c-4070-ad95-4be975eeef1e.svg'
AUTHOR = 'gpt-6'

class OneChilli(Solo48):
    icon_id = 'one-chilli'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'one-chilli')

    def build(self):
        # Plan: Preserve the bent pepper with a raised stem; use a flowing taper and rounded shoulder.
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
        path('pepper',(4,29),[('C',(32,17),(16,34),(24,23)),('C',(40,19),(35,12),(40,15)),('C',(18,40),(45,29),(33,40)),('C',(4,29),(11,40),(6,35))],True)
        path('stem',(40,19),[('C',(44,8),(43,17),(44,13))]);join('stem','pepper')
