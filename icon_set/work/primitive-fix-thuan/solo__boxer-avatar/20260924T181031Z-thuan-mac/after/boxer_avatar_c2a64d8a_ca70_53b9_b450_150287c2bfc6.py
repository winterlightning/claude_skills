from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c2a64d8a-ca70-53b9-b450-150287c2bfc6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxer-avatar/20260924T181031Z-thuan-mac/reference/boxer_c2a64d8a-ca70-53b9-b450-150287c2bfc6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'boxer-avatar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('boxer',)
    # Plan: Boxer in a guard pose with large padded gloves and narrow wrist cuffs; mirrored gloves share dimensions.
    # Construction references: Shared human_ref/full_body_ref.png: detached circular head and round-ended limbs; Lucide hand-fist: one continuous fist silhouette.
    # Omissions: Headguard omitted in favor of the conventional boxing-glove cue; head-to-torso ink gap is exactly 4px.
    def build(self):
        # Raised boxing gloves flank the guarded figure. One glove definition mirrored.
        self.circle('head',24,14,6)
        self.add_line('torso',(24,28),(24,40))
        self.mark_human_figure('boxer',head='head',torso='torso',torso_junction='start')
        for i,cx in enumerate((10,38)):
            self.path(f'glove-{i}',(cx-6,29),[((cx+6,29),6,6,True),(cx+6,32),(cx+6,36),(cx+4,40),(cx-4,40),(cx-6,36),(cx-6,32),(cx-6,29)],True)
            node=(cx+6,32) if i==0 else (cx-6,32)
            self.add_line(f'arm-{i}',(24,28),node)
            self.relate('connect',f'arm-{i}',f'glove-{i}')
            self.relate('connect',f'arm-{i}','torso')
        self.relate('connect','arm-0','arm-1')

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
