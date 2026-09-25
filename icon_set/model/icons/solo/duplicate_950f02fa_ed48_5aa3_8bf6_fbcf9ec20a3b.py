"""Two overlapping rounded squares, offset diagonally.
Construction reference: copy: consistent corner radii and partial rear outline.
Reduction: No omissions; intentional diagonal offset preserves depth.
Keyshape: SQUARE; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '950f02fa-ed48-5aa3-8bf6-fbcf9ec20a3b'
SOURCE_PATH = 'icon_set/work/todo-references/duplicate_950f02fa-ed48-5aa3-8bf6-fbcf9ec20a3b.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'duplicate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('duplicate',)

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
        # Plan: front square split at the rear-square attachment points.
        self.path('front',(10,6),[(28,6),((32,10),4,4,True),(32,16),(32,28),((28,32),4,4,True),(16,32),(10,32),((6,28),4,4,True),(6,10),((10,6),4,4,True)],True)
        self.path('rear',(32,16),[(38,16),((42,20),4,4,True),(42,38),((38,42),4,4,True),(20,42),((16,38),4,4,True),(16,32)])
        self.relate('connect','front','rear')
