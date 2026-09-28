from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '404190ff-389e-4a15-a7fe-4b448b432ffd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handcuffs-with-arched-connector'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('handcuffs',)
    # Plan: Two broad closed cuffs with narrow lock housings and an arched chain; mirrored about x=24.
    # Construction references: Original handcuffs: lock housings and enlarged cuff openings.
    # Omissions: Double ring thickness omitted.
    def build(self):
        for i,cx in enumerate((12,36)):
            self.path(f'cuff-{i}',(cx-4,18),[(cx,18),(cx+4,18),(cx+4,24),((cx+8,30),8,8,True),((cx-8,30),8,10,True),((cx-4,24),8,8,True),(cx-4,18)],True)
        self.path('chain',(12,18),[((24,8),12,10,True),((36,18),12,10,True)])
        for i in range(2): self.relate('connect','chain',f'cuff-{i}')

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
