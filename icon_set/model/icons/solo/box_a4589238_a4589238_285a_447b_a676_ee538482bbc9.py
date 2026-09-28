"""box-a4589238: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4589238-285a-447b-a676-ee538482bbc9'
SOURCE_PATH = 'pictographic-primitives/shipping/box_a4589238-285a-447b-a676-ee538482bbc9.svg'
AUTHOR = 'gpt-6'

class BoxA4589238(Solo48):
    icon_id = 'box-a4589238'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    categories = ('primitives', 'shipping')
    aliases = ()
    keywords = ('box', 'shipping', 'solo-ai-next50')

    def build(self):
        # Plan: A tall paper carton has pitched shoulders and a right-side gusset. The gusset starts below the top fold, removing a tiny triangular opening while preserving real package depth.
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
        poly('carton',(8,14),(16,4),(30,4),(40,14),(40,44),(30,44),(8,44),closed=True)
        poly('fold',(8,14),(30,14),(40,14));line('side',(30,14),(30,44));join('fold','carton');join('side','carton');join('side','fold')
