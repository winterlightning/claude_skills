from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e88b736-a624-5653-bfe9-0df39a7adb24'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/cat 1_3e88b736-a624-5653-bfe9-0df39a7adb24.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cartoon-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('cat 1',)
    # Plan: Pointed ears, broad rounded cheeks, paired eyes and a feline nose; vertical mirror axis x=24.
    # Construction references: Lucide cat: pointed ears joined to cheek contour and sparse facial marks.
    # Omissions: Whiskers omitted to preserve clear space.
    def build(self):
        # Mirrored ears, circular lower face, paired eyes and a small central nose.
        self.path('face',(6,24),[(8,6),(18,14),(30,14),(40,6),(42,24),((6,24),18,18,True)],True)
        for x in (16,32):self.add_dot(f'eye-{x}',(x,24))
        self.add_polyline('nose',(22,31),(24,33),(26,31))

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
