"""arrow-wayfinding: Continuous rounded return arrow; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5762ca4d-99c2-4016-910c-36aa0e18889f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/arrow_5762ca4d-99c2-4016-910c-36aa0e18889f.svg'
AUTHOR = 'gpt-6'

class ArrowWayfinding(Solo48):
    icon_id = 'arrow-wayfinding'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('solo-ai-full-set', 'arrow-wayfinding')

    def build(self):
        # Plan: A single semicircular turn meets horizontal runs tangentially; both wings share the arrow point.
        # Reference: Lucide undo-2: original and atomic-debug geometry.

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
        path('shaft',(25,8),[('L',(33,8)),('A',(33,30),11,11,True),('L',(4,30))])
        path('head',(14,20),[('L',(4,30)),('L',(14,40))])
        join('shaft','head')
