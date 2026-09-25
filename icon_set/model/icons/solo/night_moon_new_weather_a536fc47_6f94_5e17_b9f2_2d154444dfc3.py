"""night-moon-new-weather: Smooth crescent silhouette; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a536fc47-6f94-5e17-b9f2-2d154444dfc3'
SOURCE_PATH = 'pictographic-primitives/weather/night moon new_a536fc47-6f94-5e17-b9f2-2d154444dfc3.svg'
AUTHOR = 'gpt-6'

class NightMoonNewWeather(Solo48):
    icon_id = 'night-moon-new-weather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'night-moon-new-weather')

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
        def pt(x,y):return (48-x,y) if True else (x,y)
        path('moon',pt(8,4),[('C',pt(40,24),pt(27,4),pt(40,12)),('C',pt(8,44),pt(40,36),pt(27,44)),('C',pt(25,24),pt(20,41),pt(25,32)),('C',pt(8,4),pt(25,16),pt(20,7))],True)
