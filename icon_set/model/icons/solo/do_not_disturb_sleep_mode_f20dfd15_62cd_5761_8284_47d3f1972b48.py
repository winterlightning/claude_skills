"""do-not-disturb-sleep-mode: Smooth diagonal crescent; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f20dfd15-62cd-5761-8284-47d3f1972b48'
SOURCE_PATH = 'pictographic-primitives/mobile/do not disturb sleep mode_f20dfd15-62cd-5761-8284-47d3f1972b48.svg'
AUTHOR = 'gpt-6'

class DoNotDisturbSleepMode(Solo48):
    icon_id = 'do-not-disturb-sleep-mode'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'do-not-disturb-sleep-mode')

    def build(self):
        # Plan: Preserve the diagonal moon with its upper-left and lower-right horns; replace the fitted lumps with flowing curves.
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
        path('moon',(21,6),[('C',(6,24),(12,8),(6,15)),('C',(24,42),(6,34),(14,42)),('C',(42,32),(32,42),(38,39)),('C',(21,6),(19,41),(10,18))],True)
