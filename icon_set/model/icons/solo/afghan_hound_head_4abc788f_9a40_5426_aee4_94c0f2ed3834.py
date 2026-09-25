from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4abc788f-9a40-5426-aee4-94c0f2ed3834'
SOURCE_PATH = 'pictographic-primitives/pets/afghan hound_4abc788f-9a40-5426-aee4-94c0f2ed3834.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'afghan-hound-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/pets'
    aliases = ()
    keywords = ('afghan hound',)
    # Plan: Afghan hound in three-quarter view: a long muzzle framed by a large flowing asymmetric coat arch and one eye.
    # Construction references: Original Afghan hound: long hair and elongated muzzle; Lucide dog: minimal face marks.
    # Omissions: Nose and hair striations omitted; smallest permitted eye is one 4px dot.
    def build(self):
        # Long asymmetric coat arch; one eye inside the long muzzle, with no smile.
        self.path('coat',(8,44),[(8,24),((22,4),14,20,True),((40,24),18,20,True),(40,44)])
        self.path('muzzle',(19,16),[(17,31),((27,39),10,8,False),(30,33),(30,44)])
        self.add_dot('eye',(27,23))

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
