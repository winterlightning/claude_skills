"""house-with-roof-flag: Small pitched-roof shelter with a doorway and roof-mounted flag. House mirrors x20; flag remains deliberately offset right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '994ac35b-40e3-5aa4-a436-b3ffec189ed6'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors shelter home_994ac35b-40e3-5aa4-a436-b3ffec189ed6.svg'
AUTHOR = 'gpt-6'


class HouseWithRoofFlag(Solo48):
    icon_id = 'house-with-roof-flag'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('house', 'shelter', 'flag', 'home', 'base', 'camp', 'building', 'outdoors-batch-02')

    def build(self):
        # Plan: Small pitched-roof shelter with a doorway and roof-mounted flag. House mirrors x20; flag remains deliberately offset right.
        # Lucide house original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (4, 8, 44, 40).
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
        poly('roof',(4,30),(8,28),(20,22),(28,26),(32,28),(36,30))
        poly('walls',(8,28),(8,40),(16,40),(16,32),(24,32),(24,40),(32,40),(32,28));join('walls','roof')
        poly('flag',(28,26),(28,16),(28,8),(44,8),(44,16),(28,16));join('flag','roof')
