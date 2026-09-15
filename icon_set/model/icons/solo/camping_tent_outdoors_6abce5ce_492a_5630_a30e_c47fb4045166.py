"""camping-tent-outdoors: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6abce5ce-492a-5630-a30e-c47fb4045166'
SOURCE_PATH = 'icons-json/outdoors/camping tent_6abce5ce-492a-5630-a30e-c47fb4045166.json'
AUTHOR = 'gpt-6'

class CampingTentOutdoors(Solo48):
    icon_id = 'camping-tent-outdoors'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('camping', 'tent', 'outdoors', 'solo-ai-next100')

    def build(self):
        # Plan: Retain the arched dome tent, with matching outer slopes and a roomy arched entrance.
        # Reference: Lucide tent original and atomic-debug construction.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
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
        path('tent',(6,42),[('C',(24,6),(10,24),(16,6)),('C',(42,42),(32,6),(38,24)),('L',(32,42)),('L',(16,42)),('L',(6,42))],True)
        path('door',(16,42),[('C',(24,20),(17,30),(20,20)),('C',(32,42),(28,20),(31,30))]);join('door','tent')
