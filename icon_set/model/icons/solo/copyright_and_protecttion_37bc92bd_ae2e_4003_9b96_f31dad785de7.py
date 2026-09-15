"""copyright-and-protecttion: Centered registered mark; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '37bc92bd-ae2e-4003-9b96-f31dad785de7'
SOURCE_PATH = 'pictographic-primitives/content/copyright and protecttion_37bc92bd-ae2e-4003-9b96-f31dad785de7.svg'
AUTHOR = 'gpt-6'

class CopyrightAndProtecttion(Solo48):
    icon_id = 'copyright-and-protecttion'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('solo-ai-full-set', 'copyright-and-protecttion')

    def build(self):
        # Plan: Keep the R inside a true circle; widen its diagonal leg angle to avoid a pinched lower counter.
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
        circle('ring',24,24,20)
        path('bowl',(18,24),[('L',(18,14)),('L',(24,14)),('A',(24,24),5,5,True),('L',(18,24))],True)
        line('stem',(18,24),(18,33));line('leg',(24,24),(31,32));join('stem','bowl');join('leg','bowl')
