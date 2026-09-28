"""laptop small squares: fresh SOLO48 repair.
Plan: Widened screen and sloped base make the laptop explicit; two detached marks echo the source's small tiles.
Keyshape: HRECT_L. The two marks sit side by side to preserve clean spacing.
Omissions: Fine box outlines reduce to two marks at the strict 48-pixel stroke.
Construction reference: No useful additional Lucide match inspected; supplied laptop reference governs construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '71714a04-dd1b-4fab-90a6-dbd391dacaf5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laptop-small-squares/20260927T142540Z-thuan-mac-1/reference/laptop small squares_71714a04-dd1b-4fab-90a6-dbd391dacaf5.svg'
AUTHOR = "gpt-6"
PARENT_SOURCE = 'icon_set/model/icons/solo/laptop_small_squares_71714a04_dd1b_4fab_90a6_dbd391dacaf5.py'

class Drawing(Solo48):
    icon_id = 'laptop-small-squares'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('laptop small squares',)

    def laptop(self):
        self.add_line('screen-left', (8, 32), (8, 12))
        self.add_arc('screen-tl', (8, 12), (12, 8), radius_x=4)
        self.add_line('screen-top', (12, 8), (36, 8))
        self.add_arc('screen-tr', (36, 8), (40, 12), radius_x=4)
        self.add_line('screen-right', (40, 12), (40, 32))
        self.add_line('hinge', (40, 32), (8, 32))
        self.add_contour('screen', 'screen-left', 'screen-tl', 'screen-top', 'screen-tr', 'screen-right', 'hinge', closed=True)
        self.add_polyline('base', (8, 32), (4, 40), (44, 40), (40, 32))
        self.relate('connect', 'screen', 'base')

    def build(self):
        self.laptop()
        for i, x in enumerate((18, 30)):
            self.add_dot('tile-' + str(i), (x, 20))
