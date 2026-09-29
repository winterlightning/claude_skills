"""corn: Broad cob and overlapping husks; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfc9df01-8144-40e0-b66d-be471956d900'
SOURCE_PATH = 'pictographic-primitives/food/corn_dfc9df01-8144-40e0-b66d-be471956d900.svg'
AUTHOR = 'gpt-6'

class Corn(Solo48):
    icon_id = 'corn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('food', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-shapes-refine', 'solo-ai-next100', 'corn')

    def build(self):
        # Plan: Restore a broad rounded cob tapering behind overlapping husks. The wider crown and asymmetric leaf overlap preserve the original ear-of-corn reading.
        # Reference: Original football; exact mirrored panel construction.

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
        path('cob',(18,25),[('L',(16,12)),('A',(32,12),8,8,True),('L',(30,25))])
        path('husk',(8,22),[('C',(18,25),(12,22),(15,23)),('C',(24,31),(20,27),(22,29)),('C',(30,25),(26,29),(28,27)),('C',(40,22),(33,23),(36,22)),('C',(24,44),(37,35),(38,44)),('C',(20,43),(22,44),(21,44)),('C',(8,22),(11,40),(11,32))],True)
        path('overlap',(24,31),[('C',(20,43),(21,35),(20,39))]);join('overlap','husk');join('husk','cob')
