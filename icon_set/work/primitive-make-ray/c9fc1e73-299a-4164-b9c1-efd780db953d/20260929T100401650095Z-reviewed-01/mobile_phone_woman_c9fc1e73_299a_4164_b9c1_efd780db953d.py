from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c9fc1e73-299a-4164-b9c1-efd780db953d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-woman/20260929T094854Z-thuan-mac/reference/mobile phone woman_c9fc1e73-299a-4164-b9c1-efd780db953d.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mobile-phone-woman'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'A recognizable handset needs its speaker and home dot in addition to the woman portrait. Compact hair/face/shoulder contacts and spacing within the phone are visually clear at 48px in both themes.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': '844d5d9ce8c2c689f4bcae6746d1c556b39727d12c27d5d103690dd3cb05c6dd'}
    aliases = ()
    keywords = ()
    # Plan: Restore a recognizable smartphone with speaker, home dot and an inset woman portrait with hair.
    # Original/current comparison: The portrait dominates a generic frame and the device lacks a clear speaker or home control; feedback specifically asks for Phone.
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
        self.line('speaker',(21,10),(27,10))
        self.circle('face',24,22,5)
        self.path('hair-left',(19,21), [('L',(18,26)),('L',(16,29))])
        self.path('hair-right',(29,21), [('L',(30,26)),('L',(32,29))])
        self.path('shoulders',(16,35), [('A',(32,35),8,4,True)])
        self.add_dot('home',(24,40))
