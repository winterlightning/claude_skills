"""box-shipping: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20c6ed49-886d-4ca0-b960-c8322bf94767'
SOURCE_PATH = 'pictographic-primitives/shipping/box_20c6ed49-886d-4ca0-b960-c8322bf94767.svg'
AUTHOR = 'gpt-6'

class BoxShipping(Solo48):
    icon_id = 'box-shipping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping', 'solo-ai-next50')

    def build(self):
        # Plan: A sealed shipping cube shows a narrow band crossing its top plane. Two sloping faces and a single front corner preserve the package perspective.
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
        poly('carton',(6,16),(15,11),(24,6),(42,16),(42,32),(24,42),(6,32),closed=True)
        poly('rim',(6,16),(24,26),(33,21),(42,16));line('corner',(24,26),(24,42));join('rim','carton');join('corner','rim');join('corner','carton')
        # A second top-panel seam keeps the tape broad enough to read.
        line('tape',(15,11),(33,21));join('tape','carton');join('tape','rim')
