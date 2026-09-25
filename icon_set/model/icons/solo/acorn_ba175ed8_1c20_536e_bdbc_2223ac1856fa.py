"""acorn: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ba175ed8-1c20-536e-bdbc-2223ac1856fa'
SOURCE_PATH = 'pictographic-primitives/food/acorn_ba175ed8-1c20-536e-bdbc-2223ac1856fa.svg'
AUTHOR = 'gpt-6'

class Acorn(Solo48):
    icon_id = 'acorn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('acorn', 'food', 'solo-ai-first50')

    def build(self):
        # Plan: A symmetric cap owns its midpoint stem and two body attachments; a single smooth nut tapers to the bottom extreme. Removed conversion wiggles.
        # Reference: Lucide original/nut.svg and atomic-debug/nut.svg.

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
        axis = 24
        path('cap', (8,24), [('A',(axis,12),16,12,True),('A',(40,24),16,12,True),('L',(36,24)),('L',(12,24)),('L',(8,24))],True)
        path('nut',(12,24), [('C',(24,44),(12,37),(18,40)),('C',(36,24),(30,40),(36,37))])
        line('stem',(24,4),(24,12))
        join('stem','cap'); join('nut','cap')

