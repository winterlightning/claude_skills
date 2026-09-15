"""delivery-truck: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '168c20b9-0f99-5089-9ebf-e13c3a71cdc9'
SOURCE_PATH = 'icons-json/delivery/delivery truck_168c20b9-0f99-5089-9ebf-e13c3a71cdc9.json'
AUTHOR = 'gpt-6'

class DeliveryTruck(Solo48):
    icon_id = 'delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'delivery'
    aliases = ()
    keywords = ('delivery', 'truck', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the tall cargo compartment and short cab. Round tyres attach cleanly below the body, while a sloped or squared cab preserves the variant.
        # Reference: Lucide truck original and atomic-debug construction.

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
        path('body',(4,8),[('L',(28,8)),('L',(28,16)),('L',(38,16)),('L',(44,21)),('L',(44,28)),('A',(40,32),4,4,True),('L',(36,32)),('L',(28,32)),('L',(12,32)),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,8))],True)
        line('partition',(28,16),(28,32));join('partition','body')

        for x in (12,36):
         path(f'wheel-{x}',(x,32),[('A',(x+4,36),4,4,True),('A',(x,40),4,4,True),('A',(x-4,36),4,4,True),('A',(x,32),4,4,True)],True)
         join(f'wheel-{x}','body')
