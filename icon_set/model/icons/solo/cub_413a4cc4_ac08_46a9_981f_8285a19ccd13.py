"""cub: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '413a4cc4-ac08-46a9-981f-8285a19ccd13'
SOURCE_PATH = 'icons-json/_uncategorized_13/cub_413a4cc4-ac08-46a9-981f-8285a19ccd13.json'
AUTHOR = 'gpt-6'

class Cub(Solo48):
    icon_id = 'cub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('cub', '_uncategorized', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the isometric box as three broad faces with a shared center junction. Top-face depth differentiates the original variant.
        # Reference: Lucide box original and atomic-debug construction.

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
        poly('box',(24,6),(42,16),(42,32),(24,42),(6,32),(6,16),closed=True)
        poly('seams',(6,16),(24,26),(42,16));line('vertical',(24,26),(24,42));join('seams','box');join('vertical','seams');join('vertical','box')
