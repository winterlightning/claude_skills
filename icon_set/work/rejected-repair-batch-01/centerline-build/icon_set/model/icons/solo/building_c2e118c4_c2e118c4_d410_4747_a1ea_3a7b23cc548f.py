"""building-c2e118c4: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2e118c4-d410-4747-a1ea-3a7b23cc548f'
SOURCE_PATH = 'pictographic-primitives/building/building_c2e118c4-d410-4747-a1ea-3a7b23cc548f.svg'
AUTHOR = 'gpt-6'

class BuildingC2e118c4(Solo48):
    icon_id = 'building-c2e118c4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the asymmetric sloped roof and low left annex. The roof mast and facade meet at exact nodes.
        # Reference: Lucide building-2 original and atomic-debug construction.

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
        poly('tower',(22,42),(22,6),(36,15),(42,19),(42,42),(6,42),(6,22),(22,22));join('tower','tower')
        line('mast',(36,6),(36,15));join('mast','tower')
        line('window',(6,32),(12,32));join('window','tower')
