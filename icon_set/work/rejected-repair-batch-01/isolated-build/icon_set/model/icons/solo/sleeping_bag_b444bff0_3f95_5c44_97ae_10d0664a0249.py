"""sleeping-bag: Upright sleeping bag with rounded hood and foot, a circular hood opening, and one lower seam; extra quilting omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b444bff0-3f95-5c44-97ae-10d0664a0249'
SOURCE_PATH = 'pictographic-primitives/outdoors/camping sleeping bag_b444bff0-3f95-5c44-97ae-10d0664a0249.svg'
AUTHOR = 'gpt-6'


class SleepingBag(Solo48):
    icon_id = 'sleeping-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('sleeping-bag', 'camping', 'sleep', 'outdoors', 'bedroll', 'gear', 'rest', 'outdoors-batch-01')

    def build(self):
        # Plan: Upright sleeping bag with rounded hood and foot, a circular hood opening, and one lower seam; extra quilting omitted.
        # Lucide backpack: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (8, 4, 40, 44).

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
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('bag',(8,20),[('A',(40,20),16,16,True),('L',(40,34)),('A',(30,44),10,10,True),('L',(18,44)),('A',(8,34),10,10,True),('L',(8,20))],True)
        circle('hood',24,19,6)
        line('seam',(8,34),(40,34));join('seam','bag')
