"""Two overlapping conversation boxes with opposing tails.
Construction reference: messages-square: offset bubbles and angular speech tails.
Reduction: No defining features omitted.
Keyshape: SQUARE; geometry authored directly on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '37e6c825-f29a-4cbb-9920-8bf21012a299'
SOURCE_PATH = 'icon_set/work/todo-references/double comment box_37e6c825-f29a-4cbb-9920-8bf21012a299.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'double-comment-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('double', 'comment', 'box')

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
        # Plan: front box owns junctions for the partly occluded rear box.
        self.path('front',(10,6),[(28,6),((32,10),4,4,True),(32,18),(32,22),((28,26),4,4,True),(22,26),(12,34),(12,26),(6,26),(6,10),((10,6),4,4,True)],True)
        self.path('rear',(32,18),[(42,18),(42,34),(36,34),(36,42),(26,34),(22,34),(22,26)])
        self.relate('connect','front','rear')
