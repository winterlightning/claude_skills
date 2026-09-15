"""astronomy-planet-pluto: Smooth planetary contour; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '538b81e2-4f12-5deb-8847-decaad176f32'
SOURCE_PATH = 'pictographic-primitives/science/astronomy planet pluto_538b81e2-4f12-5deb-8847-decaad176f32.svg'
AUTHOR = 'gpt-6'

class AstronomyPlanetPluto(Solo48):
    icon_id = 'astronomy-planet-pluto'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('solo-ai-full-set', 'astronomy-planet-pluto')

    def build(self):
        # Plan: Preserve the asymmetric inner loop inside a true circular planet; attach it at exact rim nodes.
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
        path('rim',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        path('surface',(44,24),[('C',(30,16),(37,24),(37,16)),('C',(22,26),(23,16),(20,21)),('C',(28,34),(22,30),(27,31)),('C',(24,44),(29,38),(26,41))]);join('surface','rim')
