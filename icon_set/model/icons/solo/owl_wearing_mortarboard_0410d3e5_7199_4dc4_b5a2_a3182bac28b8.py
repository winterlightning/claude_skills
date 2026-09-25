from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0410d3e5-7199-4dc4-b5a2-a3182bac28b8'
SOURCE_PATH = 'pictographic-primitives/school-learning/study owl_0410d3e5-7199-4dc4-b5a2-a3182bac28b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'owl-wearing-mortarboard'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'education/school'
    aliases = ()
    keywords = ('study owl',)
    # Plan: Owl face with two large circular eyes and a pointed beak beneath its mortarboard.
    # Construction references: Lucide graduation-cap: diamond brim and tassel; original study owl: large paired round eyes and small beak.
    # Omissions: Body and wing outline omitted to preserve the owl-specific eyes and beak at 48px.
    def build(self):
        # Owl face: two large open eye disks and a pointed beak under a diamond cap.
        self.add_polyline('cap',(8,10),(24,4),(40,10),(24,16),(8,10))
        for x in (14,34):self.circle(f'eye-{x}',x,28,5)
        self.add_polyline('beak',(21,40),(24,44),(27,40))
        self.add_line('tassel',(8,10),(8,16));self.relate('connect','cap','tassel')

    def path(self, name, start, steps, closed=False):
        current = start
        ids = []
        for index, step in enumerate(steps):
            ident = f"{name}-{index}"
            if len(step) == 2:
                self.add_line(ident, current, step)
                current = step
            else:
                end, rx, ry, sweep = step
                self.add_arc(ident, current, end, radius_x=rx, radius_y=ry, sweep=sweep)
                current = end
            ids.append(ident)
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name, (cx-r,cy), [((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)], True)

    def box(self, name, x, y, w, h, r=3):
        self.path(name,(x+r,y),[(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),
            ((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)],True)
