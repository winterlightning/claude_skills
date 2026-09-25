from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4679969c-dfb9-4a03-ab57-4d2eded56e5a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__batch-01-laptop-computers/20260924T181031Z-thuan-mac/reference/laptop_4679969c-dfb9-4a03-ab57-4d2eded56e5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'batch-01-laptop-computers'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('laptop',)
    # Plan: One laptop: rounded upright screen and a broad flared keyboard base; extremes (4,8)-(44,40).
    # Construction references: Lucide laptop: screen and flared base with shared hinge.
    # Omissions: Keyboard keys omitted at 48px.
    def build(self):
        self.path('body',(8,30),[(8,12),((12,8),4,4,True),(36,8),((40,12),4,4,True),(40,30),(44,40),(4,40),(8,30)],True)
        self.add_line('hinge',(8,30),(40,30))
        self.relate('connect','body','hinge')

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
