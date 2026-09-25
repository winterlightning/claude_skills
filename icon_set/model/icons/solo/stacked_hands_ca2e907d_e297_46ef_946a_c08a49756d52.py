from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca2e907d-e297-46ef-946a-c08a49756d52'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork hand gather_ca2e907d-e297-46ef-946a-c08a49756d52.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stacked-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('workflow teamwork hand gather',)
    # Plan: Overlapping palms entered by visible wrists replace the angular central knot.
    # Construction references: Original stacked hands: an upper wrist and a diagonally crossing palm; Lucide hand: rounded finger turn.
    # Omissions: Finger seams reduced to preserve the overlapping-hand reading.
    def build(self):
        # A top wrist enters from above; a second palm approaches diagonally from right.
        self.path('lower-hand',(14,6),[(14,20),((6,28),8,8,False),((14,36),8,8,False),(16,42)])
        self.path('upper-wrist',(28,6),[(28,15),(34,21)])
        self.path('top-hand',(42,42),[(34,34),(22,22),((16,28),5,5,False),(24,36),(18,36),(6,42)])
        self.add_polyline('fingers',(34,21),(42,29))
        self.relate('connect','fingers','upper-wrist')

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
