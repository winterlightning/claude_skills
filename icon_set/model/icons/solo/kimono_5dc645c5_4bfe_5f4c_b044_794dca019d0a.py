"""kimono: Balanced wrapped kimono; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5dc645c5-4bfe-5f4c-b044-794dca019d0a'
SOURCE_PATH = 'pictographic-primitives/sports/kimono_5dc645c5-4bfe-5f4c-b044-794dca019d0a.svg'
AUTHOR = 'gpt-6'

class Kimono(Solo48):
    icon_id = 'kimono'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'kimono')

    def build(self):
        # Plan: Preserve wide sleeves, crossed lapels and flared skirt. Use a single diagonal wrap across a broad waist.
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
        path('garment',(6,18),[('L',(18,6)),('L',(30,6)),('L',(42,18)),('L',(37,25)),('L',(32,21)),('L',(32,29)),('L',(35,42)),('L',(13,42)),('L',(16,29)),('L',(16,21)),('L',(11,25)),('L',(6,18))],True)
        path('lapel',(18,6),[('L',(24,19)),('L',(30,6))]);join('lapel','garment')
        path('wrap',(24,19),[('L',(24,29)),('L',(32,29))]);join('wrap','lapel');join('wrap','garment');line('belt',(16,29),(24,29));join('belt','wrap');join('belt','garment')
