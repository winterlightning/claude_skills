from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a430fc9d-29f3-4753-b308-1283a45b63e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-stopwatch/20260924T181031Z-thuan-mac/reference/workflow coaching stopwatch hand_a430fc9d-29f3-4753-b308-1283a45b63e1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-stopwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('workflow coaching stopwatch hand',)
    # Plan: Rounded palm, extended thumb, open wrist and stacked curled fingers restore the hand silhouette.
    # Construction references: Lucide hand and hand-fist: shared finger joints and rounded knuckles; original coaching hand reference.
    # Omissions: Four fingers and stopwatch dial must remain recognizable; this fit tests their spacing.
    def build(self):
        # Wrist is open at left; continuous thumb/palm contour and four rounded fingers at right.
        self.path('hand',(8,28),[(16,20),(20,8),((28,8),4,4,True),(28,12),(36,12),
            ((36,20),4,4,True),((36,28),4,4,True),((36,36),4,4,True),((36,44),4,4,True),(8,44)])
        for y in (20,28,36):
            self.add_line(f'crease-{y}',(28,y),(36,y));self.relate('connect','hand',f'crease-{y}')
        self.circle('stopwatch',20,30,8)
        self.add_polyline('watch-hand',(20,25),(20,30),(23,33))

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
