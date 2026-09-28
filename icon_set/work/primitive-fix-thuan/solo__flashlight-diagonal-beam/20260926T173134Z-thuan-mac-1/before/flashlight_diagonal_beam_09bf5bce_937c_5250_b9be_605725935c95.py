"""flashlight-diagonal-beam: Diagonal flashlight with flared lens head and a forward beam. Angled silhouette is intentional; switch and second small ray omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09bf5bce-937c-5250-b9be-605725935c95'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors flashlight_09bf5bce-937c-5250-b9be-605725935c95.svg'
AUTHOR = 'gpt-6'


class FlashlightDiagonalBeam(Solo48):
    icon_id = 'flashlight-diagonal-beam'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('flashlight', 'torch', 'light', 'beam', 'camping', 'battery', 'outdoors', 'outdoors-batch-02')

    def build(self):
        # Plan: Diagonal flashlight with flared lens head and a forward beam. Angled silhouette is intentional; switch and second small ray omitted.
        # Lucide flashlight original and atomic-debug inspected for construction.
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
        poly('flashlight',(4,30),(14,40),(26,28),(34,28),(38,24),(22,8),(18,12),(18,16),closed=True)
        line('beam',(40,12),(44,8))
