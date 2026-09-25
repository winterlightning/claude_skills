"""cargo-ship-symbol: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab3ea798-6eb7-4962-94f0-08838f608e51'
SOURCE_PATH = 'pictographic-primitives/symbol/cargo ship_ab3ea798-6eb7-4962-94f0-08838f608e51.svg'
AUTHOR = 'gpt-6'

class CargoShipSymbol(Solo48):
    icon_id = 'cargo-ship-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('cargo', 'ship', 'symbol', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the frontal ship and stepped deckhouse. The deckhouse rests directly on a level gunwale above the low bow waves.
        # Reference: Lucide ship original and atomic-debug construction.

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
        poly('cabin',(12,23),(12,14),(19,14),(19,6),(29,6),(29,14),(36,14),(36,23))
        poly('hull',(10,39),(6,23),(12,23),(36,23),(42,23),(38,39));join('hull','cabin')
        poly('water',(6,42),(10,39),(17,42),(24,39),(31,42),(38,39),(42,42));join('water','hull')
