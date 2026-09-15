"""armchair: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '049cac05-52fa-5b8f-9a6e-d5ee4caeceb0'
SOURCE_PATH = 'pictographic-primitives/furnitures/armchair_049cac05-52fa-5b8f-9a6e-d5ee4caeceb0.svg'
AUTHOR = 'gpt-6'

class Armchair(Solo48):
    icon_id = 'armchair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('armchair', 'furnitures', 'solo-ai-first50')

    def build(self):
        # Plan: A rounded back joins a continuous upholstered arm-and-seat contour at matching nodes. Shared dimensions keep both armrests and legs equal; removed tiny arm loops.
        # Reference: Lucide original/armchair.svg and atomic-debug/armchair.svg.

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
        path('back',(12,20), [('L',(12,16)),('A',(36,16),12,12,True),('L',(36,20))])
        path('seat',(12,20), [('L',(8,20)),('L',(8,32)),('A',(12,36),4,4,False),('L',(36,36)),('A',(40,32),4,4,False),('L',(40,20)),('L',(36,20)),('L',(32,20)),('L',(32,28)),('L',(16,28)),('L',(16,20)),('L',(12,20))],True)
        join('back','seat')
        for x in (12,36):
         line(f'leg-{x}',(x,36),(x,44));join(f'leg-{x}','seat')

