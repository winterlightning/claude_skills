from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5b320b4e-ed89-4f2f-be89-6e9fdbbeecce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__meeting-headphone-wireless-solo/20260929T094854Z-thuan-mac/reference/meeting headphone wireless_5b320b4e-ed89-4f2f-be89-6e9fdbbeecce.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'meeting-headphone-wireless-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore two earcups, a headband, boom microphone and two nested wireless arcs.
    # Original/current comparison: The old headset has dots instead of earcups and a detached arc/dot resembling a person, losing wireless meeting context.
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
        self.path('signal-outer',(12,10), [('A',(36,10),17,12,True)])
        self.path('signal-inner',(19,13), [('A',(29,13),9,6,True)])
        self.path('band',(9,31), [('A',(39,31),15,12,True)])
        self.rect('cup-left',6,28,7,12,3)
        self.rect('cup-right',35,28,7,12,3)
        self.path('boom',(38,40), [('A',(30,44),8,4,True),('L',(21,44))])
