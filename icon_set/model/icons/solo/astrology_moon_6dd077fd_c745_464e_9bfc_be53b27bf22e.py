"""astrology-moon: Smooth crescent silhouette; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6dd077fd-c745-464e-9bfc-be53b27bf22e'
SOURCE_PATH = 'pictographic-primitives/religion/astrology moon_6dd077fd-c745-464e-9bfc-be53b27bf22e.svg'
AUTHOR = 'gpt-6'

class AstrologyMoon(Solo48):
    icon_id = 'astrology-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    categories = ('primitives', 'religion')
    aliases = ()
    keywords = ('solo-ai-full-set', 'astrology-moon')

    def build(self):
        # Plan: Preserve the crescent direction; coherent outer and inner curves replace the broken tip transitions.
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
        def pt(x,y):return (48-x,y) if False else (x,y)
        path('moon',pt(8,4),[('C',pt(40,24),pt(27,4),pt(40,12)),('C',pt(8,44),pt(40,36),pt(27,44)),('C',pt(25,24),pt(20,41),pt(25,32)),('C',pt(8,4),pt(25,16),pt(20,7))],True)
