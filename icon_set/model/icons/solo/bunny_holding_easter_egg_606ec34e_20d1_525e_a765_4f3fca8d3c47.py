from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '606ec34e-20d1-525e-a765-4f3fca8d3c47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/easter egg bunny_606ec34e-20d1-525e-a765-4f3fca8d3c47.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bunny-holding-easter-egg'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('easter egg bunny',)
    # Plan: Long-eared rabbit with a rounded Easter egg cradled by one paw.
    # Construction references: Lucide rabbit: long ears and spare profile; original Easter bunny: egg held on its right.
    # Omissions: Whiskers and egg decoration omitted.
    def build(self):
        # Upright bunny with two long ears and an egg cradled against its right side.
        self.path('bunny',(8,44),[(8,36),(8,24),(8,8),((16,8),4,4,True),(16,16),(24,16),(24,8),((32,8),4,4,True),(32,26)])
        self.add_dot('eye',(18,25))
        self.path('egg',(32,26),[((40,36),8,10,True),((32,44),8,8,True),((24,36),8,8,True),((32,26),8,10,True)],True)
        self.add_line('paw',(8,36),(24,36))
        self.relate('connect','bunny','egg');self.relate('connect','bunny','paw');self.relate('connect','paw','egg')

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
