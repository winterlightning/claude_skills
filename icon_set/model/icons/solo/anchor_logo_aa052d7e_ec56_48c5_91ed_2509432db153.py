"""anchor-logo: Balanced anchor; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa052d7e-ec56-48c5-91ed-2509432db153'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/anchor logo_aa052d7e-ec56-48c5-91ed-2509432db153.svg'
AUTHOR = 'gpt-6'

class AnchorLogo(Solo48):
    icon_id = 'anchor-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'anchor-logo')

    def build(self):
        # Plan: Preserve the loop, crossbar and two flukes; mirrored arms meet at the central stem and exact arrow tips.
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
        path('ring',(24,14),[('A',(20,10),4,4,True),('A',(24,6),4,4,True),('A',(28,10),4,4,True),('A',(24,14),4,4,True)],True)
        path('stem',(24,14),[('L',(24,23)),('L',(24,42))]);join('stem','ring');path('bar',(18,23),[('L',(24,23)),('L',(30,23))]);join('bar','stem')
        path('arms',(8,27),[('C',(24,42),(8,36),(16,42)),('C',(40,27),(32,42),(40,36))]);join('arms','stem')
        path('left',(6,33),[('L',(8,27)),('L',(14,31))]);path('right',(34,31),[('L',(40,27)),('L',(42,33))]);join('left','arms');join('right','arms')
