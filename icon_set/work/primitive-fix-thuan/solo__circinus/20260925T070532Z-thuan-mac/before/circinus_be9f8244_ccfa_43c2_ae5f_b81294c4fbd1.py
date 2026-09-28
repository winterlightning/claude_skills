"""circinus: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be9f8244-ccfa-43c2-ae5f-b81294c4fbd1'
SOURCE_PATH = 'pictographic-primitives/state/circinus_be9f8244-ccfa-43c2-ae5f-b81294c4fbd1.svg'
AUTHOR = 'gpt-6'

class Circinus(Solo48):
    icon_id = 'circinus'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circinus', 'state', 'solo-ai-next100')

    def build(self):
        # Plan: A drafting compass keeps its round hinge and two angled legs. The two leg spreads differ, retaining the source instrument posture.
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
        circle('hinge',32,14,8)
        line('top',(38,8),(42,6));join('top','hinge')
        poly('left-leg',(26,20),(6,32));join('left-leg','hinge')
        poly('right-leg',(34,22),(26,42));join('right-leg','hinge')
        poly('brace',(19,25),(30,32),(35,34));join('brace','left-leg');join('brace','right-leg')
