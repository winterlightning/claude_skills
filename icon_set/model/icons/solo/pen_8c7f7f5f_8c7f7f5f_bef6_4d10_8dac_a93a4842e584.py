"""pen-8c7f7f5f: Smooth pointed pen nib; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8c7f7f5f-bef6-4d10-8dac-a93a4842e584'
SOURCE_PATH = 'pictographic-primitives/design/pen_8c7f7f5f-bef6-4d10-8dac-a93a4842e584.svg'
AUTHOR = 'gpt-6'

class Pen8c7f7f5f(Solo48):
    icon_id = 'pen-8c7f7f5f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('solo-ai-full-set', 'pen-8c7f7f5f')

    def build(self):
        # Plan: Keep the teardrop nib, centered slit and diagonal stem with an exact shared shoulder node.
        # Reference: Lucide pen-tool: original and atomic-debug geometry.

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
        path('nib',(6,42),[('L',(14,18)),('C',(25,12),(17,13),(20,12)),('C',(33,15),(28,12),(31,13)),('C',(36,23),(35,17),(36,19)),('C',(30,34),(36,28),(35,31)),('L',(6,42))],True)
        line('slit',(6,42),(24,24));join('slit','nib');line('stem',(33,15),(42,6));join('stem','nib')
