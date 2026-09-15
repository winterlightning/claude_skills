"""stethoscope: Smooth stethoscope loops; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd302c6d8-a92a-4d28-bbf2-86fef555f93f'
SOURCE_PATH = 'pictographic-primitives/symbol/stethoscope_d302c6d8-a92a-4d28-bbf2-86fef555f93f.svg'
AUTHOR = 'gpt-6'

class Stethoscope(Solo48):
    icon_id = 'stethoscope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'stethoscope')

    def build(self):
        # Plan: Preserve the forked ear tubes, hanging hose and circular chestpiece; the hose meets an exact circle endpoint.
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
        path('ears',(11,6),[('L',(6,8)),('L',(6,17)),('A',(16,27),10,10,False),('A',(26,17),10,10,False),('L',(26,8)),('L',(21,6))])
        path('hose',(16,27),[('L',(16,30)),('A',(38,30),11,12,False),('L',(38,19))]);join('hose','ears')
        path('bell',(38,19),[('A',(34,15),4,4,True),('A',(38,11),4,4,True),('A',(42,15),4,4,True),('A',(38,19),4,4,True)],True);join('bell','hose')
