from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9441b8ec-57df-4f5b-8f53-e4bc68bdb94e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-field-of-view-top/20260929T093041Z-thuan-mac/reference/field of view fov top_9441b8ec-57df-4f5b-8f53-e4bc68bdb94e.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'head-field-of-view-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'The top-view field-of-view symbol needs a dashed cone and nose. Compact dash spacing and ray-to-head spacing preserve the reference arrangement at native size.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': 'e52a99204f24e37ccc1ce990b377e3fcf3c96744fa3e4d4634548487242ea6fa'}
    aliases = ()
    keywords = ()
    # Plan: Restore two dashed diverging sight rays, top-view nose and lateral ears around a round head.
    # Original/current comparison: The old view-angle strokes float beside a generic round head; the dotted cone and top-view nose are unclear.
    # References: claimed original; Lucide hand/hard-hat/ear/triangle-alert
    # construction where applicable; human_ref/user.svg and full_body_ref.png.
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

    def build(self):
        self.path('head',(22,21), [('L',(24,18)),('L',(26,21)),('A',(36,32),11,11,True),('L',(38,33)),('L',(36,35)),('A',(12,35),12,9,True),('L',(10,33)),('L',(12,32)),('A',(22,21),11,11,True)],True)
        for side in (-1,1):
            self.line(f'ray-far-{side}',(24+side*16,4),(24+side*12,9))
            self.line(f'ray-near-{side}',(24+side*8,13),(24+side*6,15))
