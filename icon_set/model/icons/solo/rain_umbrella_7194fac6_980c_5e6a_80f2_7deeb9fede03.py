"""rain-umbrella: Balanced umbrella canopy; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7194fac6-980c-5e6a-80f2-7deeb9fede03'
SOURCE_PATH = 'pictographic-primitives/weather/rain umbrella_7194fac6-980c-5e6a-80f2-7deeb9fede03.svg'
AUTHOR = 'gpt-6'

class RainUmbrella(Solo48):
    icon_id = 'rain-umbrella'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('solo-ai-full-set', 'rain-umbrella')

    def build(self):
        # Plan: Preserve three canopy scallops and the hooked handle; use mirrored canopy arcs with an exact center attachment.
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
        path('canopy',(6,24),[('C',(24,8),(9,14),(16,8)),('C',(42,24),(32,8),(39,14)),('C',(30,24),(38,20),(34,20)),('C',(24,24),(28,20),(26,20)),('C',(18,24),(22,20),(20,20)),('C',(6,24),(14,20),(10,20))],True)
        path('handle',(24,24),[('L',(24,37)),('A',(14,37),5,5,True)]);join('handle','canopy');line('tip',(24,6),(24,8));join('tip','canopy')
