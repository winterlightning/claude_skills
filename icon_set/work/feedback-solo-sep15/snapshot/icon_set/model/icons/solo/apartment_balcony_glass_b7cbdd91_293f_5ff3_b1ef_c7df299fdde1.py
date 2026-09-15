"""apartment-balcony-glass: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7cbdd91-293f-5ff3-b1ef-c7df299fdde1'
SOURCE_PATH = 'pictographic-primitives/building/apartment balcony glass_b7cbdd91-293f-5ff3-b1ef-c7df299fdde1.svg'
AUTHOR = 'gpt-6'

class ApartmentBalconyGlass(Solo48):
    icon_id = 'apartment-balcony-glass'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('apartment', 'balcony', 'glass', 'building', 'solo-ai-first50')

    def build(self):
        # Plan: A centered two-pane window rises above a continuous balcony rail; paired posts share spacing. Omitted small reflection slashes to protect the openings.
        # Reference: No useful exact Lucide match; geometric construction from the supplied subject.

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
        poly('window',(12,28),(12,8),(24,8),(36,8),(36,28))
        line('mullion',(24,8),(24,28));join('mullion','window')
        poly('rail',(4,28),(12,28),(24,28),(36,28),(44,28))
        join('rail','window');join('rail','mullion')
        for x in (12,36):
         line(f'post-{x}',(x,28),(x,40));join(f'post-{x}','rail')
        poly('base',(12,40),(36,40));join('base','post-12');join('base','post-36')

