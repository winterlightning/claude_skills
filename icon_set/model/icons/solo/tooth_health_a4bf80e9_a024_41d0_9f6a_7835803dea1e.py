"""tooth-health: Smooth tooth with floss; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4bf80e9-a024-41d0-9f6a-7835803dea1e'
SOURCE_PATH = 'pictographic-primitives/health/tooth_a4bf80e9-a024-41d0-9f6a-7835803dea1e.svg'
AUTHOR = 'gpt-6'

class ToothHealth(Solo48):
    icon_id = 'tooth-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'tooth-health')

    def build(self):
        # Plan: Preserve the tooth and attached floss tail. The crown and roots remain distinct from the separate curled floss.
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
        path('tooth',(19,9),[('C',(11,6),(15,8),(14,6)),('C',(6,15),(8,6),(6,10)),('C',(10,29),(6,20),(9,25)),('C',(13,42),(10,37),(10,42)),('C',(19,28),(17,42),(15,28)),('C',(25,42),(23,28),(21,42)),('C',(28,29),(28,42),(28,37)),('C',(32,15),(29,25),(32,20)),('C',(27,6),(32,10),(30,6)),('C',(19,9),(24,6),(23,8))],True)
        path('floss',(32,15),[('C',(40,24),(38,15),(40,19)),('L',(40,35)),('C',(42,38),(40,38),(41,39))]);join('floss','tooth')
