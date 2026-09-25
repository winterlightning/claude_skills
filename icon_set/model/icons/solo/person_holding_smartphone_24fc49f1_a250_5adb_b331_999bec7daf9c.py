from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '24fc49f1-a250-5adb-b331-999bec7daf9c'
SOURCE_PATH = 'pictographic-primitives/work/meeting smartphone hold_24fc49f1-a250-5adb-b331-999bec7daf9c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-holding-smartphone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('meeting smartphone hold',)
    # Plan: A person with a clearly separate upright smartphone supported by a bent arm.
    # Construction references: Shared human_ref/user.svg and full_body_ref.png: circular head, round shoulder and limb construction.
    # Omissions: Screen details omitted; detached head has an exact 4px ink gap.
    def build(self):
        # Detached circular head follows upper torso axis at x=16; exact gap: 26-(12+6)=8.
        self.circle('head',16,12,6)
        self.add_line('torso',(16,26),(16,42))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.path('back',(16,26),[((6,36),10,10,False),(6,42)])
        self.relate('connect','torso','back')
        self.box('phone',30,14,12,20,2)
        self.path('arm',(16,26),[(24,42),(40,42),(40,34)])
        self.relate('connect','arm','torso');self.relate('connect','arm','back');self.relate('connect','arm','phone')

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
