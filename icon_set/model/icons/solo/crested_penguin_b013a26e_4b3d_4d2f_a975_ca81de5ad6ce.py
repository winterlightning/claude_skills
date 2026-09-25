from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b013a26e-4b3d-4d2f-a975-ca81de5ad6ce'
SOURCE_PATH = 'pictographic-primitives/animals/penguin crested_b013a26e-4b3d-4d2f-a975-ca81de5ad6ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crested-penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('penguin crested',)
    # Plan: Crested penguin in side profile: upright pear body, projecting beak, long flipper, swept crest and flat foot.
    # Construction references: Original penguin: upright body, crest, beak and flipper; deliberate profile asymmetry prioritizes a conventional bird reading.
    # Omissions: Far eye, far flipper and belly patch omitted.
    def build(self):
        # Side view preserves a bird beak and long flipper without antenna-like symmetry.
        self.path('body',(32,24),[(32,32),((24,44),8,12,True),((8,32),16,12,True),((16,21),8,11,True),(16,15),((25,6),9,9,True),((34,15),9,9,True),(40,20),(32,24)],True)
        self.add_dot('eye',(25,16))
        self.add_line('flipper',(23,27),(19,34))
        self.add_line('crest',(25,6),(14,4));self.relate('connect','body','crest')
        self.add_line('foot',(24,44),(34,44));self.relate('connect','body','foot')

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
