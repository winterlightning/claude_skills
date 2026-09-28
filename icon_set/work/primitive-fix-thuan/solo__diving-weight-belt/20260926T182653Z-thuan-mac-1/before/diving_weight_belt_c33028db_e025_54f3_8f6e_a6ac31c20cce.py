"""diving-weight-belt: Belt strap with buckle and two hanging weights. Weight size and spacing share a row definition. Buckle slots omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c33028db-e025-54f3-8f6e-a6ac31c20cce'
SOURCE_PATH = 'pictographic-primitives/outdoors/diving weight belt_c33028db-e025-54f3-8f6e-a6ac31c20cce.svg'
AUTHOR = 'gpt-6'


class DivingWeightBelt(Solo48):
    icon_id = 'diving-weight-belt'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('weight-belt', 'diving', 'scuba', 'belt', 'weights', 'gear', 'buckle', 'outdoors-batch-01')

    def build(self):
        # Plan: Belt strap with buckle and two hanging weights. Weight size and spacing share a row definition. Buckle slots omitted.
        # Lucide backpack: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (4, 8, 44, 40).

        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',((x0+x1)//2,y0)),('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('strap',(4,8),(24,8),(44,8),(44,20),(36,20),(24,20),(12,20),(4,20),closed=True)
        line('buckle',(24,8),(24,20));join('buckle','strap')
        for i,x in enumerate((6,30)):
            rounded(f'weight-{i}',x,28,x+12,40,3)
            line(f'hanger-{i}',(x+6,20),(x+6,28));join(f'hanger-{i}','strap');join(f'hanger-{i}',f'weight-{i}')
