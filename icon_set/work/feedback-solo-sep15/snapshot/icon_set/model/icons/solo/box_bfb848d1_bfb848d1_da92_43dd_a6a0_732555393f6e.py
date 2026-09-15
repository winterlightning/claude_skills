"""box-bfb848d1: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bfb848d1-da92-43dd-a6a0-732555393f6e'
SOURCE_PATH = 'pictographic-primitives/shipping/box_bfb848d1-da92-43dd-a6a0-732555393f6e.svg'
AUTHOR = 'gpt-6'

class BoxBfb848d1(Solo48):
    icon_id = 'box-bfb848d1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping', 'solo-ai-next50')

    def build(self):
        # Plan: A landscape taped parcel has a wide integral closure with a square end. The shallow box and flat tape distinguish it from the V-cut vertical package.
        # Reference: Lucide package original and atomic-debug construction.

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
        poly('carton',(4,8),(18,8),(30,8),(44,8),(44,40),(4,40),closed=True)
        poly('tape',(18,8),(18,24),(30,24),(30,8));join('tape','carton')
