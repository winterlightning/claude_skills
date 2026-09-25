"""ant-uncategorized-03: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '30ad0906-c2eb-4948-9c07-8924910b00e8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/ant_30ad0906-c2eb-4948-9c07-8924910b00e8.svg'
AUTHOR = 'gpt-6'

class AntUncategorized03(Solo48):
    icon_id = 'ant-uncategorized-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('ant', '_uncategorized_03', 'solo-ai-first50')

    def build(self):
        # Plan: A circular head has exact antenna junctions; a generous gap separates it from the rounded body. Paired antennae and legs are derived from one axis.
        # Reference: Lucide original/bug.svg and atomic-debug/bug.svg.

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
        path('head',(21,9), [('A',(27,9),5,5,True),('A',(29,13),5,5,True),('A',(19,13),5,5,True),('A',(21,9),5,5,True)],True)
        path('body',(18,31), [('A',(24,27),6,4,True),('A',(30,31),6,4,True),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,31))],True)
        for side in (-1,1):
         x=lambda d:24+side*d
         line(f'antenna-{side}',(x(3),9),(x(10),4));join(f'antenna-{side}','head')
         poly(f'leg-top-{side}',(x(6),31),(x(12),27),(x(16),31))
         poly(f'leg-bottom-{side}',(x(6),38),(x(12),36),(x(16),44))
         join(f'leg-top-{side}','body');join(f'leg-bottom-{side}','body')

