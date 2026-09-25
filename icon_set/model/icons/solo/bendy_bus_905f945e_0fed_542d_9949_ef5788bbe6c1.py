"""bendy-bus: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '905f945e-0fed-542d-9949-ef5788bbe6c1'
SOURCE_PATH = 'pictographic-primitives/transportation/bendy bus_905f945e-0fed-542d-9949-ef5788bbe6c1.svg'
AUTHOR = 'gpt-6'

class BendyBus(Solo48):
    icon_id = 'bendy-bus'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('bendy', 'bus', 'transportation', 'solo-ai-first50')

    def build(self):
        # Plan: A rounded bus body has integrated wheel arches and two matching circular wheels. The chassis joins exact left/right wheel endpoints; windows share one horizontal band.
        # Reference: Lucide original/bus.svg and atomic-debug/bus.svg.

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
        path('body',(4,32), [('L',(4,12)),('A',(8,8),4,4,True),('L',(16,8)),('L',(28,8)),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,24)),('L',(44,32)),('L',(40,32)),('L',(32,32)),('L',(16,32)),('L',(8,32)),('L',(4,32))],True)
        poly('window-base',(4,24),(16,24),(28,24),(44,24));join('window-base','body')
        for x in (16,28):
         line(f'pillar-{x}',(x,8),(x,24));join(f'pillar-{x}','body');join(f'pillar-{x}','window-base')
        for x in (12,36):
         path(f'wheel-{x}',(x-4,32), [('L',(x-4,36)),('A',(x+4,36),4,4,False),('L',(x+4,32))])
         join(f'wheel-{x}','body')

