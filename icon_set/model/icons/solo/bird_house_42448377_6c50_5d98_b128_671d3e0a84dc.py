"""bird-house: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42448377-6c50-5d98-b128-671d3e0a84dc'
SOURCE_PATH = 'pictographic-primitives/interface-essential/bird house_42448377-6c50-5d98-b128-671d3e0a84dc.svg'
AUTHOR = 'gpt-6'

class BirdHouse(Solo48):
    icon_id = 'bird-house'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('bird', 'house', 'interface-essential', 'solo-ai-next50')

    def build(self):
        # Plan: A symmetric roof sits over a broader nesting box and a clearly open circular entrance. The opening has nine units of centerline clearance from both side walls.
        # Reference: Lucide birdhouse original and atomic-debug construction.

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
        poly('roof',(8,20),(10,18),(24,4),(38,18),(40,20))
        poly('house',(10,18),(10,44),(38,44),(38,18));join('roof','house')
        circle('entrance',24,28,5)
