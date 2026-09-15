"""hiking-backpack: Rounded hiking bag with carry handle, flap seam and broad front pocket. Main silhouette mirrors x24; side pockets and small buckle omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b36b69a-6a46-53b0-8fa9-0be915f9f94d'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors backpack_1b36b69a-6a46-53b0-8fa9-0be915f9f94d.svg'
AUTHOR = 'gpt-6'


class HikingBackpack(Solo48):
    icon_id = 'hiking-backpack'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('backpack', 'hiking', 'rucksack', 'camping', 'travel', 'bag', 'outdoors', 'outdoors-batch-02')

    def build(self):
        # Plan: Rounded hiking bag with carry handle, flap seam and broad front pocket. Main silhouette mirrors x24; side pockets and small buckle omitted for clearance.
        # Lucide backpack original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (8, 4, 40, 44).
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
        path('bag',(16,12),[('L',(32,12)),('A',(40,20),8,8,True),('L',(40,24)),('L',(40,36)),('A',(32,44),8,8,True),('L',(16,44)),('A',(8,36),8,8,True),('L',(8,24)),('L',(8,20)),('A',(16,12),8,8,True)],True)
        poly('handle',(16,12),(16,4),(32,4),(32,12));join('handle','bag')
        line('flap',(8,24),(40,24));join('flap','bag')
        poly('pocket',(16,44),(16,32),(32,32),(32,44));join('pocket','bag')
