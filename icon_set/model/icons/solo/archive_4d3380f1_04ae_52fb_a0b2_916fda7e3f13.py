"""archive: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d3380f1-04ae-52fb-a0b2-916fda7e3f13'
SOURCE_PATH = 'pictographic-primitives/content/archive_4d3380f1-04ae-52fb-a0b2-916fda7e3f13.svg'
AUTHOR = 'gpt-6'

class Archive(Solo48):
    icon_id = 'archive'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('archive', 'content', 'solo-ai-first50')

    def build(self):
        # Plan: A wide lid and centered handle sit on a rounded storage box. Shared rim nodes preserve real attachment; corners use equal radii.
        # Reference: Lucide original/archive.svg and atomic-debug/archive.svg.

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
        poly('lid',(4,8),(44,8),(44,16),(40,16),(8,16),(4,16),closed=True)
        path('body',(8,16), [('L',(8,36)),('A',(12,40),4,4,False),('L',(36,40)),('A',(40,36),4,4,False),('L',(40,16))])
        line('handle',(20,27),(28,27));join('lid','body')

