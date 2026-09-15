"""ceiling-lamp-double: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '326638cb-38f2-5e62-8dca-bfeecd92203f'
SOURCE_PATH = 'pictographic-primitives/lamps/ceiling lamp double_326638cb-38f2-5e62-8dca-bfeecd92203f.svg'
AUTHOR = 'gpt-6'

class CeilingLampDouble(Solo48):
    icon_id = 'ceiling-lamp-double'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    aliases = ()
    keywords = ('ceiling', 'lamp', 'double', 'lamps', 'solo-ai-next100')

    def build(self):
        # Plan: A two-shade ceiling fixture uses one mirrored shade definition and matching hanging arms.
        # Reference: Lucide lamp-ceiling original and atomic-debug construction.

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
        line('ceiling',(14,8),(34,8));line('stem',(24,8),(24,20));join('stem','ceiling')
        path('arms',(12,28),[('L',(12,24)),('A',(16,20),4,4,True),('L',(24,20)),('L',(32,20)),('A',(36,24),4,4,True),('L',(36,28))]);join('arms','stem')
        for x in (12,36):
         path(f'shade-{x}',(x-8,40),[('L',(x-5,31)),('C',(x,28),(x-4,29),(x-2,28)),('C',(x+5,31),(x+2,28),(x+4,29)),('L',(x+8,40)),('L',(x-8,40))],True);join(f'shade-{x}','arms')
