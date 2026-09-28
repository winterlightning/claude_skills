"""hurricane-oil-lantern: Bulging oil lantern with narrow top cap and central flame. Shared mirrored chamber; handle band, inner curl and extra foot line omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e26b4fae-5159-5626-a3fd-b6d33103328d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hurricane-oil-lantern/20260927T070849Z-thuan-mac-1/reference/outdoors flame lantern_e26b4fae-5159-5626-a3fd-b6d33103328d.svg'
AUTHOR = "gpt-6"


class HurricaneOilLantern(Solo48):
    icon_id = 'hurricane-oil-lantern'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('lantern', 'oil-lamp', 'hurricane', 'flame', 'camping', 'light', 'outdoors', 'outdoors-batch-02')

    def build(self):
        # Plan: Bulging oil lantern with narrow top cap and central flame. Shared mirrored chamber; handle band, inner curl and extra foot line omitted.
        # Lucide flame original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (8, 4, 40, 44).
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        # Rebuild the source's tall side guards and broad flat foot.
        self.add_bezier('frame-left-upper',(16,12),((10,18),(8,24),(8,30)))
        self.add_bezier('frame-left-lower',(8,30),((8,37),(9,44),(12,44)))
        self.add_line('frame-bottom',(12,44),(36,44))
        self.add_bezier('frame-right-lower',(36,44),((39,44),(40,37),(40,30)))
        self.add_bezier('frame-right-upper',(40,30),((40,24),(38,18),(32,12)))
        self.add_contour('frame','frame-left-upper','frame-left-lower','frame-bottom','frame-right-lower','frame-right-upper')
        poly('cap',(12,12),(12,4),(36,4),(36,12),closed=True)
        join('cap','frame')
        path('flame',(24,22),[('A',(28,30),12,12,True),('A',(20,30),4,4,True),('A',(24,22),12,12,True)],True)
