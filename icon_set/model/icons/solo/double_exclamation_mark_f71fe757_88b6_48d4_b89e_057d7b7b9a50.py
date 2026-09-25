"""Two straight exclamation marks with outlined circular dots.
Construction reference: circle-alert: separated stem and dot, with the supplied outlined dot retained.
Reduction: No defining features omitted.
Keyshape: VRECT_L; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f71fe757-88b6-48d4-b89e-057d7b7b9a50'
SOURCE_PATH = 'icon_set/work/todo-references/double exclamation mark_f71fe757-88b6-48d4-b89e-057d7b7b9a50.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'double-exclamation-mark-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('double', 'exclamation', 'mark')

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
        # Plan: two equal punctuation symbols share top, baseline and radius.
        for x in (12,36):
            self.add_line(f'stem-{x}',(x,4),(x,24))
            self.circle(f'dot-{x}',x,40,4)
