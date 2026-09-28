"""bandaid: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d6f2522-2f4b-4001-af2d-ea58f858d927'
SOURCE_PATH = 'pictographic-primitives/health/bandaid_1d6f2522-2f4b-4001-af2d-ea58f858d927.svg'
AUTHOR = 'gpt-6'

class Bandaid(Solo48):
    icon_id = 'bandaid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('bandaid', 'health', 'solo-ai-first50')

    def build(self):
        # Plan: Two crossed bandages form a unified outline with smooth capsule ends and a central diamond pad; all quadrant extrema lie exactly on the square envelope.
        # Reference: Lucide original/bandage.svg and atomic-debug/bandage.svg.

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
        path('cross',(6,12), [('C',(12,6),(6,8),(8,6)),('C',(17,9),(14,6),(15,7)),('L',(24,16)),('L',(31,9)),('C',(36,6),(33,7),(34,6)),('C',(42,12),(40,6),(42,8)),('C',(39,17),(42,14),(41,15)),('L',(32,24)),('L',(39,31)),('C',(42,36),(41,33),(42,34)),('C',(36,42),(42,40),(40,42)),('C',(31,39),(34,42),(33,41)),('L',(24,32)),('L',(17,39)),('C',(12,42),(15,41),(14,42)),('C',(6,36),(8,42),(6,40)),('C',(9,31),(6,34),(7,33)),('L',(16,24)),('L',(9,17)),('C',(6,12),(7,15),(6,14))],True)
        poly('pad',(24,16),(32,24),(24,32),(16,24),closed=True);join('cross','pad')

