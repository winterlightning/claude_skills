from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '52c708f4-a507-499a-ba67-b97481d798ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-storefront-batch-025-05/20260929T094944Z-thuan-mac/reference/mobile shop 1_52c708f4-a507-499a-ba67-b97481d798ed.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mobile-storefront-batch-025-05'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Keep the phone frame/home control and recognizable scalloped shop awning. Compact scallop openings and shop/frame spacing are intentional and readable at 48px.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': '2c1bedb711c0c7fcf357339381b706dabd26b4c2fc315557449a615d929cb22f'}
    aliases = ()
    keywords = ()
    # Plan: Restore a rounded mobile frame, scalloped shop awning, screen window and separate bottom home control.
    # Original/current comparison: The storefront fills the whole handset and has no home control; the drawing reads as a generic shop.
    # References: claimed original; Lucide smartphone/lock-open/headset/memory-stick/drone
    # original and atomic-debug where applicable; human_ref/user.svg and full_body_ref.png.
    # Paired anatomical parts share parameters; directional profiles stay asymmetric.

    def path(self, name, start, steps, closed=False):
        members = []
        here = start
        for i, step in enumerate(steps):
            member = f"{name}-{i}"
            if step[0] == "L":
                self.add_line(member, here, step[1])
            else:
                self.add_arc(member, here, step[1], radius_x=step[2], radius_y=step[3], sweep=step[4])
            here = step[1]
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)], True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), [("A",(x+rx,y),rx,ry,True),("A",(x-rx,y),rx,ry,True)], True)

    def poly(self, name, *points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def line(self, name, a, b):
        self.add_line(name, a, b)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),[("L",(x+w-r,y)),("A",(x+w,y+r),r,r,True),("L",(x+w,y+h-r)),("A",(x+w-r,y+h),r,r,True),("L",(x+r,y+h)),("A",(x,y+h-r),r,r,True),("L",(x,y+r)),("A",(x+r,y),r,r,True)],True)

    def phone(self):
        self.rect('phone',10,4,28,40,4)
        self.add_line('screen-bottom',(10,36),(38,36))
        self.relate('connect','phone','screen-bottom')

    def wireless(self):
        self.add_arc('signal-outer',(8,9),(40,9),radius_x=24,radius_y=16,sweep=True)
        self.add_arc('signal-inner',(17,14),(31,14),radius_x=12,radius_y=9,sweep=True)

    def build(self):
        self.rect('phone',8,4,32,40,4)
        self.path('awning',(12,16), [('L',(16,10)),('L',(32,10)),('L',(36,16)),('A',(28,16),4,4,True),('A',(20,16),4,4,True),('A',(12,16),4,4,True)],True)
        self.poly('shop-front',(15,23),(15,33),(33,33),(33,23))
        self.add_dot('home',(24,39))
