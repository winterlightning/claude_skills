"""chocolate-box: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bcab073e-f7dd-439e-8a8a-e72d016006a4'
SOURCE_PATH = 'pictographic-primitives/romance/chocolate box_bcab073e-f7dd-439e-8a8a-e72d016006a4.svg'
AUTHOR = 'gpt-6'

class ChocolateBox(Solo48):
    icon_id = 'chocolate-box'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('chocolate', 'box', 'romance', 'solo-ai-next100')

    def build(self):
        # Plan: A heart-shaped chocolate box retains broad lobes and a clear lower depth band; symmetric curves meet the heart valley and point.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        path('lid',(24,13),[('C',(14,8),(20,10),(18,8)),('C',(4,16),(8,8),(4,10)),('L',(24,28)),('L',(44,16)),('C',(34,8),(44,10),(40,8)),('C',(24,13),(30,8),(28,10))],True)
        poly('depth',(4,16),(4,28),(24,40),(44,28),(44,16));line('seam',(24,28),(24,40));join('depth','lid');join('seam','depth');join('seam','lid')
