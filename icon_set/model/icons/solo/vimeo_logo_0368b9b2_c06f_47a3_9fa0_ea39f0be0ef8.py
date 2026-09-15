"""vimeo-logo: Looping V — local spacing refinement; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0368b9b2-c06f-47a3-9fa0-ea39f0be0ef8'
SOURCE_PATH = 'pictographic-primitives/logos/vimeo logo_0368b9b2-c06f-47a3-9fa0-ea39f0be0ef8.svg'
AUTHOR = 'gpt-6'

class VimeoLogo(Solo48):
    icon_id = 'vimeo-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('solo-ai-full-set', 'vimeo-logo')

    def build(self):
        # Plan: Kept every original curve. Adjusted the inner hook and its handles to open the counter.
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
        path('mark',(4,17),[('C',(17,8),(9,12),(13,8)),('C',(22,22),(21,8),(21,17)),('C',(24,29),(23,27),(22,31)),('C',(31,18),(28,25),(31,21)),('C',(29,15),(32,14),(30,12)),('C',(44,14),(34,7),(43,8)),('C',(22,40),(44,25),(29,40)),('C',(14,29),(17,40),(16,34)),('L',(11,18)),('L',(4,17))],True)
