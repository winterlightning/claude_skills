"""pile-poo: Smooth stacked swirl; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c335382e-9874-5d16-95d4-344cff747084'
SOURCE_PATH = 'pictographic-primitives/smileys/pile poo_c335382e-9874-5d16-95d4-344cff747084.svg'
AUTHOR = 'gpt-6'

class PilePoo(Solo48):
    icon_id = 'pile-poo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'pile-poo')

    def build(self):
        # Plan: Preserve the three-tier swirl and curled top; use a broad rounded base and draw each shared edge once.
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
        path('base',(13,28),[('L',(35,28)),('A',(35,42),7,7,True),('L',(13,42)),('A',(13,28),7,7,True)],True)
        path('middle',(13,28),[('C',(12,22),(9,27),(9,24)),('C',(19,18),(13,18),(15,18)),('L',(30,18)),('C',(35,28),(36,18),(39,25))]);join('middle','base')
        path('top',(19,18),[('C',(24,6),(19,14),(29,13)),('C',(33,14),(29,7),(33,9)),('C',(30,18),(33,16),(31,18))]);join('top','middle')
