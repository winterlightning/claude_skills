"""wattpad-logo: Regular outlined W; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e11fe56a-f394-4b99-94e0-187e60406c37'
SOURCE_PATH = 'pictographic-primitives/logos/wattpad logo_e11fe56a-f394-4b99-94e0-187e60406c37.svg'
AUTHOR = 'gpt-6'

class WattpadLogo(Solo48):
    icon_id = 'wattpad-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'wattpad-logo')

    def build(self):
        # Plan: Preserve the three upright bars and rounded lower-left return; use consistent slot and stem widths.
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
        path('mark',(4,8),[('L',(12,8)),('L',(12,28)),('A',(14,30),2,2,False),('L',(20,30)),('L',(20,8)),('L',(28,8)),('L',(28,30)),('L',(36,30)),('L',(36,8)),('L',(44,8)),('L',(44,40)),('L',(16,40)),('A',(4,28),12,12,True),('L',(4,8))],True)
