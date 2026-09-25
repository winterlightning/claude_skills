from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd972c303-2754-4efe-82ae-c0b2f535370b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bowling-pins-row/20260924T181031Z-thuan-mac/reference/three bowlings_d972c303-2754-4efe-82ae-c0b2f535370b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bowling-pins-row'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('three bowlings',)
    # Plan: Three continuous bowling-pin outlines: rounded crown, narrow neck, lower belly, flat base; shared shape and spacing.
    # Construction references: Original three bowling pins: continuous pin silhouettes; no useful local Lucide bowling-pin match.
    # Omissions: Neck stripes omitted; neck width is the anticipated blocking constraint.
    def build(self):
        # One continuous pin definition repeated on 16-unit centers; no touching loops.
        for i,cx in enumerate((8,24,40)):
            self.path(f'pin-{i}',(cx-3,11),[((cx+3,11),3,3,True),(cx+2,18),(cx+2,22),
                ((cx+4,30),4,8,True),(cx+3,38),((cx+1,40),2,2,True),(cx-1,40),
                ((cx-3,38),2,2,True),(cx-4,30),((cx-2,22),4,8,True),(cx-2,18),(cx-3,11)],True)

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
