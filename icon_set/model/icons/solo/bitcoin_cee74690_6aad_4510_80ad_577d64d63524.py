"""bitcoin: Regular Bitcoin letterform; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cee74690-6aad-4510-80ad-577d64d63524'
SOURCE_PATH = 'pictographic-primitives/symbol/bitcoin_cee74690-6aad-4510-80ad-577d64d63524.svg'
AUTHOR = 'gpt-6'

class Bitcoin(Solo48):
    icon_id = 'bitcoin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('solo-ai-full-set', 'bitcoin')

    def build(self):
        # Plan: Preserve the double vertical bars, serifs and two B bowls; share all crossing nodes and equalize the counter widths.
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
        path('upper',(16,9),[('L',(24,9)),('L',(28,9)),('C',(40,17),(36,9),(40,12)),('C',(28,25),(40,22),(36,25)),('L',(24,25)),('L',(16,25)),('L',(16,9))],True)
        path('lower',(16,25),[('L',(16,41)),('L',(24,41)),('L',(28,41)),('C',(40,33),(36,41),(40,38)),('C',(28,25),(40,28),(36,25))]);join('lower','upper')
        for name,y in [('top',9),('bottom',41)]:line(name,(8,y),(16,y));join(name,'upper' if y==9 else 'lower')
        line('left-top',(16,4),(16,9));line('left-bottom',(16,41),(16,44));join('left-top','upper');join('left-bottom','lower')
        path('right',(24,4),[('L',(24,9)),('L',(24,25)),('L',(24,41)),('L',(24,44))]);join('right','upper');join('right','lower')
