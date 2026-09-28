from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '135d01ca-c11c-4e70-a645-04b5dbcd9502'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-handshake/20260924T181031Z-thuan-mac/reference/workflow teamwork handshake_135d01ca-c11c-4e70-a645-04b5dbcd9502.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-handshake'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('workflow teamwork handshake',)
    # Plan: Two hands meet diagonally, with a curved clasping thumb and rounded finger edge.
    # Construction references: Lucide handshake: two opposing palms, inset thumb and scalloped fingers.
    # Omissions: Fourth finger and second visible thumb require additional room; tested in the repair loop.
    def build(self):
        # Opposed cuffs, curved central thumb and a scalloped lower finger edge.
        self.path('outer',(4,16),[(12,8),(22,12),(30,8),(44,18),(38,28),
            ((32,34),5,5,True),((26,38),4,4,True),((18,40),5,5,True),(4,26),(4,16)],True)
        self.path('thumb',(30,8),[(20,18),((26,24),5,5,False),(30,20),(38,28)])
        self.relate('connect','outer','thumb')
        self.add_line('finger-1',(26,28),(32,34));self.relate('connect','outer','finger-1')
        self.add_line('finger-2',(20,32),(26,38));self.relate('connect','outer','finger-2')

    def path(self, name, start, steps, closed=False):
        current = start
        ids = []
        for index, step in enumerate(steps):
            ident = f"{name}-{index}"
            if len(step) == 2:
                self.add_line(ident, current, step)
                current = step
            else:
                end, rx, ry, sweep = step
                self.add_arc(ident, current, end, radius_x=rx, radius_y=ry, sweep=sweep)
                current = end
            ids.append(ident)
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name, (cx-r,cy), [((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)], True)

    def box(self, name, x, y, w, h, r=3):
        self.path(name,(x+r,y),[(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),
            ((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)],True)
