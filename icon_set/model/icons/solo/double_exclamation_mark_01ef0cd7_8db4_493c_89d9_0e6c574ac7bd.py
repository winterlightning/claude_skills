"""Two outlined tapered exclamation marks with circular dots.
Construction reference: circle-alert: vertical punctuation alignment; tapered outlines are from the supplied reference.
Reduction: No defining features omitted.
Keyshape: SQUARE; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01ef0cd7-8db4-493c-89d9-0e6c574ac7bd'
SOURCE_PATH = 'icon_set/work/todo-references/double exclamation mark_01ef0cd7-8db4-493c-89d9-0e6c574ac7bd.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'double-exclamation-mark'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
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
        # Plan: repeat a tapered outlined stem and outlined dot about x=24.
        for x in (12,36):
            self.path(f'stem-{x}',(x-6,12),[((x+6,12),6,6,True),(x,24),(x-6,12)],True)
            self.circle(f'dot-{x}',x,38,4)
