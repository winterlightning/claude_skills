"""A circular frame divided into four sectors by a diagonal cross.
Construction reference: circle-x: circular enclosure and paired crossing diagonals; source diagonals connect to the rim.
Reduction: No omissions. Diagonal attachment points use an integer 12-16-20 circle triangle.
Keyshape: CIRCLE; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56e61485-e96e-4abc-979b-4c528e31a3d1'
SOURCE_PATH = 'icon_set/work/todo-references/eclipse frame_56e61485-e96e-4abc-979b-4c528e31a3d1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'eclipse-frame'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('eclipse', 'frame')

    def path(self, name, start, segments, closed=False):
        members = []
        for i, spec in enumerate(segments):
            part = f"{name}-{i+1}"
            if len(spec) == 2:
                end = spec
                self.add_line(part, start, end)
            else:
                end, rx, ry, sweep = spec
                self.add_arc(part, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
            members.append(part)
            start = end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [((x+r,y),r,r,True),((x-r,y),r,r,True)], True)

    def rect(self, name, x, y, w, h, r=3):
        self.path(name, (x+r,y), [(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)], True)

    def build(self):
        # Plan: circle split at integer attachment points; paired diagonals share the center.
        r=20
        self.path('rim',(12,8),[((36,8),r,r,True),((36,40),r,r,True),((12,40),r,r,True),((12,8),r,r,True)],True)
        self.add_polyline('diagonal-a',(12,8),(24,24),(36,40))
        self.add_polyline('diagonal-b',(36,8),(24,24),(12,40))
        self.relate('connect','diagonal-a','diagonal-b')
        self.relate('connect','diagonal-a','rim')
        self.relate('connect','diagonal-b','rim')
