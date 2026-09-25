from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f66072f8-69df-452b-b63d-912a999c4271'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/sphere_f66072f8-69df-452b-b63d-912a999c4271.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-display-globe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('sphere',)
    # Plan: Cloud displayed inside a glass globe with a distinct rounded pedestal.
    # Construction references: Original sphere: globe and pedestal; Lucide cloud: continuous lobes and flat cloud base.
    # Omissions: Minor cloud lobes reduced.
    def build(self):
        # Glass dome on a pedestal, containing one three-lobed cloud.
        self.path('globe',(12,36),[((8,20),4,16,True),((24,4),16,16,True),((40,20),16,16,True),((36,36),4,16,True)])
        self.box('base',8,36,32,8,4)
        self.relate('connect','globe','base')
        self.path('cloud',(21,27),[((21,19),4,4,True),((27,19),3,3,True),((27,27),4,4,True),(21,27)],True)

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
