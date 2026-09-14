"""architecture-fence: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd123c4cf-199d-51d0-90b0-8f81734338b8'
SOURCE_PATH = 'icons-json/building/architecture fence_d123c4cf-199d-51d0-90b0-8f81734338b8.json'
AUTHOR = 'gpt-6'

class ArchitectureFenceVariant2(Solo48):
    icon_id = 'architecture-fence-v2'
    variant_of = 'architecture-fence'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('architecture', 'fence', 'building', 'solo-ai-first50')

    def build(self):
        # Plan: Two matching pickets use shared heights and width; two rails attach at exact endpoints. Removed uneven picket corners.
        # Reference: Lucide original/fence.svg and atomic-debug/fence.svg.

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
        for x in (8,30):
         poly(f'picket-{x}',(x,40),(x,24),(x,16),(x,14),(x+5,8),(x+10,14),(x+10,16),(x+10,24),(x+10,40),closed=True)
        for y in (16,24):
         for j,(a,b) in enumerate(((4,8),(18,30),(40,44))):
          line(f'rail-{y}-{j}',(a,y),(b,y))
          if j<2:join(f'rail-{y}-{j}','picket-8')
          if j>0:join(f'rail-{y}-{j}','picket-30')

