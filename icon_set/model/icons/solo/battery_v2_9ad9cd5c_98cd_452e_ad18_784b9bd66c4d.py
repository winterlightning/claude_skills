"""battery: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ad9cd5c-98cd-452e-ad18-784b9bd66c4d'
SOURCE_PATH = 'icons-json/photography/battery_9ad9cd5c-98cd-452e-ad18-784b9bd66c4d.json'
AUTHOR = 'gpt-6'

class BatteryVariant2(Solo48):
    icon_id = 'battery-v2'
    variant_of = 'battery'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('battery', 'photography', 'solo-ai-first50')

    def build(self):
        # Plan: A vertical cell has a rounded body and a broad terminal, with exact terminal-to-body attachments.
        # Reference: Lucide original/battery.svg and atomic-debug/battery.svg.

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
        path('body',(12,12), [('L',(16,12)),('L',(32,12)),('L',(36,12)),('A',(40,16),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,16)),('A',(12,12),4,4,True)],True)
        poly('terminal',(16,12),(16,4),(32,4),(32,12));join('terminal','body')

