"""arm-flex: Smooth flexed arm; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90cac3c3-16d4-5ca2-95e6-98d1851e462d'
SOURCE_PATH = 'pictographic-primitives/health/arm flex_90cac3c3-16d4-5ca2-95e6-98d1851e462d.svg'
AUTHOR = 'gpt-6'

class ArmFlex(Solo48):
    icon_id = 'arm-flex'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'arm-flex')

    def build(self):
        # Plan: Human reference: full_body_ref.png. Preserve the bent arm and curled fist; keep broad muscle curves and a clear inner forearm.
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
        path('arm',(40,44),[('L',(12,44)),('C',(8,38),(8,44),(8,41)),('L',(11,17)),('C',(18,11),(12,14),(15,13)),('L',(29,4)),('C',(35,12),(32,6),(35,9)),('C',(24,20),(35,17),(29,20)),('L',(19,21)),('L',(19,31)),('C',(35,31),(25,30),(30,30)),('C',(40,29),(38,28),(39,29))])
