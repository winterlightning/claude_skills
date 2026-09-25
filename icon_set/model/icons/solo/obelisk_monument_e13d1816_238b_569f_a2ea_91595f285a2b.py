"""obelisk-monument: Tapered pointed obelisk on one broad plinth. Mirrored shaft and plinth about x24; extra base band omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e13d1816-238b-569f-a2ea-91595f285a2b'
SOURCE_PATH = 'pictographic-primitives/outdoors/landmarks monument_e13d1816-238b-569f-a2ea-91595f285a2b.svg'
AUTHOR = 'gpt-6'


class ObeliskMonument(Solo48):
    icon_id = 'obelisk-monument'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('obelisk', 'monument', 'landmark', 'memorial', 'tower', 'stone', 'historic', 'outdoors-batch-02')

    def build(self):
        # Plan: Tapered pointed obelisk on one broad plinth. Mirrored shaft and plinth about x24; extra base band omitted.
        # Lucide landmark original and atomic-debug inspected for construction.
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
        axis=24
        poly('monument',(8,44),(8,36),(14,36),(16,12),(axis,4),(32,12),(34,36),(40,36),(40,44),closed=True)
        line('plinth',(14,36),(34,36));join('plinth','monument')
