from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1c0f91c5-ddcd-4057-9258-33ab46aaac34'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-euro-sign/20260929T094944Z-thuan-mac/reference/mobile phone euro sign_1c0f91c5-ddcd-4057-9258-33ab46aaac34.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mobile-phone-euro-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Keep the recognizable euro with two crossbars inside the phone. The crossbars have a 1px visible gap; native light/dark inspection confirms both and the open C remain legible.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': 'ea50f3260fabdac3099a30561b4eca41a6a7e804898f2f7ae1d3eba38e22c94f'}
    aliases = ()
    keywords = ()
    # Plan: Restore a euro with two crossbars inside a rounded handset with a bottom bezel.
    # Original/current comparison: The currency mark is a thick C with one bar and the handset corners are square.
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
        self.phone()
        self.path('euro',(30,14), [('L',(28,14)),('A',(20,22),8,8,False),('A',(28,30),8,8,False),('L',(30,30))])
        self.line('bar-top',(17,20),(27,20))
        self.line('bar-bottom',(17,25),(27,25))
