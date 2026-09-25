from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6f5654b6-d336-40f6-84c1-e153d3ad1fc3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-gripping-wrists/20260924T181031Z-thuan-mac/reference/workflow teamwork hand lock_6f5654b6-d336-40f6-84c1-e153d3ad1fc3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-gripping-wrists'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('workflow teamwork hand lock',)
    # Plan: Four open-ended wrists and hooked palms form a cooperative hand lock around a central opening.
    # Construction references: Original hand-lock reference: four hands cyclically gripping wrists; Lucide hand: finger/palm ownership.
    # Omissions: Individual finger creases initially omitted; grasp silhouettes must carry the concept.
    def build(self):
        # Four perpendicular hands grasp the next wrist around an open center.
        for i in range(4):
            def rot(p):
                x,y=p
                for _ in range(i):x,y=48-y,x
                return x,y
            pts=[(6,6),(24,6),(28,10),(28,18),(20,18),(20,14),(6,14)]
            self.add_polyline(f'hand-{i}',*[rot(p) for p in pts])

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
